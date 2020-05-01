for file in files/binaries/*; do
	upx-3.96-amd64_linux/upx -1 -q -o "files/packed_upx/${file}" $file
done
