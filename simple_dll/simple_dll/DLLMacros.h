#pragma once

#define DLL_CALLCONV __cdecl
#ifdef SIMPLEDLL_EXPORT
	#define DLL_EXPORT __declspec(dllexport) 
#else
	#define DLL_EXPORT __declspec(dllimport)
#endif

// Support C for matlab imports
#ifdef __cplusplus
#define CDLL_EXPORT extern "C" DLL_EXPORT
#else
#define CDLL_EXPORT DLL_EXPORT
#endif
