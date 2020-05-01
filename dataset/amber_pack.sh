for file in files/packed_amber/*; do
	amber_linux_amd64_2.0/amber $file
done
