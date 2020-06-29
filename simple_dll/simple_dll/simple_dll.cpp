#include <simple_dll/simple_dll.h>
#include <iostream>

#include "DLLMacros.h"


CDLL_EXPORT void printSmth()
{
    std::cout << "Something" << std::endl;
}
