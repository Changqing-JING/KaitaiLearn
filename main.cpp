#include "gen/animal_record.h"
#include <fstream>
#include <iostream>

int main() {
    std::ifstream is("build/animal_record.bin", std::ifstream::binary);
    kaitai::kstream ks(&is);

    animal_record_t animal(&ks);

    std::cout<<animal.uuid()<< " "<<animal.name()<< " "<< animal.birth_year()<< " " <<animal.weight() << " "<< animal.rating()<<std::endl;
    
    return 0; 
}