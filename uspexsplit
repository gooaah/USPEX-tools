# Split USPEX output POSCARS, transform the POSCARs into cif files, print their symmetry in the SYMM
#!/bin/bash
case "$1" in
	-g) f="goodStructures_POSCARS" ;;
	-b) f="BESTgatheredPOSCARS" ;; 
	-r) f="BESTgatheredPOSCARS_relaxed" ;;
	-i) f="gatheredPOSCARS" ;;
	*) exit ;;
esac
awk '/EA/{name = $1} {i++} {print > name }' $f
#awk '/EA/{print $1 }' $f | xargs -i vasp2cif {} 
awk '/EA/{print $1 >> "seq" }' $f
mkdir ${f}_split
mv EA* ${f}_split
mv seq ${f}_split

cd ${f}_split
#ls EA* | grep -v 'cif$' > seq
echo 'ID	SYMM' > SYMM
awk '{printf $1 >> "SYMM"} {system("phonopy --symmetry --tolerance 0.1 -c " $1 "| grep space_group_type | cut -d: -f 2 >> SYMM")}' seq
#awk '{system("phonopy --symmetry --tolerance 1 -c " $1 "| cat BPOSCAR >> gatherbpos")}' seq
rm BPOSCAR PPOSCAR seq
sed -i 's/EA//g' SYMM
cp SYMM ..

cd ..
tar -cf ${f}_split.tar ${f}_split
