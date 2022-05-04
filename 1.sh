#f_name="$(ls *.zip)"
for line in $(ls *.zip)
do
        fname=$(echo 'python3 pdf_append.py'  "$line")
	echo $($fname)
done

#for i in $(ls *jack*txt); do echo "python smoothening_matrices_comandline.py  $i"; done;

#run as ./submit.sh file_to_read job_name

