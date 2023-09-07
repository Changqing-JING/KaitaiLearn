
mkdir:
	mkdir -p build
	mkdir -p gen

ksc: mkdir
	ksc -t cpp_stl --outdir gen animal.ksy

animal_record.o: gen/animal_record.cpp
	g++ -c -g -Og -o build/$@ $<


main.bin: main.cpp animal_record.o
	g++ -g -O0 -o build/$@ $< build/animal_record.o -lkaitai_struct_cpp_stl_runtime 