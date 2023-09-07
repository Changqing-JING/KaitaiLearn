```shell
curl -LO https://github.com/kaitai-io/kaitai_struct_compiler/releases/download/0.10/kaitai-struct-compiler_0.10_all.deb
sudo apt-get install ./kaitai-struct-compiler_0.10_all.deb
git clone https://github.com/kaitai-io/kaitai_struct_cpp_stl_runtime.git
cd kaitai_struct_cpp_stl_runtime
mkdir build
cd build
cmake ..
make -j $(nproc)
sudo make install
```
