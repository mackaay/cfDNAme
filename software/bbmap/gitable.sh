#!/bin/bash

usage(){
echo "
Written by Brian Bushnell.
Last modified April 16, 2019

Description:  Creates gitable.int1d from accession files:
ftp://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/*.accession2taxid.gz
See TaxonomyGuide and fetchTaxonomy.sh for more information.

Usage:  gitable.sh shrunk.dead_nucl.accession2taxid.gz,shrunk.dead_prot.accession2taxid.gz,shrunk.dead_wgs.accession2taxid.gz,shrunk.nucl_est.accession2taxid.gz,shrunk.nucl_gb.accession2taxid.gz,shrunk.nucl_gss.accession2taxid.gz,shrunk.nucl_wgs.accession2taxid.gz,shrunk.pdb.accession2taxid.gz,shrunk.prot.accession2taxid.gz gitable.int1d.gz -Xmx24g

Java Parameters:
-Xmx            This will set Java's memory usage, overriding autodetection.
                -Xmx20g will specify 20 gigs of RAM.  The max is typically 85% of physical memory.
-eoom           This flag will cause the process to exit if an out-of-memory
                exception occurs.  Requires Java 8u92+.
-da             Disable assertions.

Please contact Brian Bushnell at bbushnell@lbl.gov if you encounter any problems.
"
}

#This block allows symlinked shellscripts to correctly set classpath.
pushd . > /dev/null
DIR="${BASH_SOURCE[0]}"
while [ -h "$DIR" ]; do
  cd "$(dirname "$DIR")"
  DIR="$(readlink "$(basename "$DIR")")"
done
cd "$(dirname "$DIR")"
DIR="$(pwd)/"
popd > /dev/null

#DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/"
CP="$DIR""current/"
NATIVELIBDIR="$DIR""jni/"

z="-Xmx24g"
z2="-Xms24g"
EA="-ea"
EOOM=""
set=0

if [ -z "$1" ] || [[ $1 == -h ]] || [[ $1 == --help ]]; then
	usage
	exit
fi

calcXmx () {
	source "$DIR""/calcmem.sh"
	parseXmx "$@"
	if [[ $set == 1 ]]; then
		return
	fi
	freeRam 24000m 84
	z="-Xmx${RAM}m"
	z2="-Xms${RAM}m"
}
calcXmx "$@"


gitable() {
	if [[ $SHIFTER_RUNTIME == 1 ]]; then
		#Ignore NERSC_HOST
		shifter=1
	elif [[ $NERSC_HOST == genepool ]]; then
		module unload oracle-jdk
		module load oracle-jdk/1.8_144_64bit
		module load pigz
	elif [[ $NERSC_HOST == denovo ]]; then
		module unload java
		module load java/1.8.0_144
		module load pigz
	elif [[ $NERSC_HOST == cori ]]; then
		module use /global/common/software/m342/nersc-builds/denovo/Modules/jgi
		module use /global/common/software/m342/nersc-builds/denovo/Modules/usg
		module unload java
		module load java/1.8.0_144
		module load pigz
	fi
	local CMD="java $EA $EOOM $z $z2 -cp $CP tax.GiToTaxid $@"
	echo $CMD >&2
	eval $CMD
}

gitable "$@"
