#pragma once

# include <cstdlib>
# include <iostream>
# include <iomanip>
# include <cmath>


//////////////////////////////////////////////////////////////////////////
//  The Ziggurat algo. generates randomly 				//
//  normal distributed numbers: 					//
//  http://people.sc.fsu.edu/~jburkardt/cpp_src/ziggurat/ziggurat.html  //
//////////////////////////////////////////////////////////////////////////

namespace Base
{
class Ziggurat
{
/*  static Ziggurat *s_instance;
  public:
  static Ziggurat &instance();
    double operator()();

  ~Ranlux();*/
public:
  static float r4_exp_value ( );
  static float efix ( );

private:
//  float efix ( );
  unsigned long int jsr_value ( );
  float nfix ( );
  void r4_exp_setup ( );
//  float r4_exp_value ( );
  void r4_nor_setup ( );
  float r4_nor_value ( );
  float r4_uni_value ( );
  unsigned long int shr3_value ( );
  void timestamp ( );
  unsigned long int ul_uni_value ( );
  void zigset ( unsigned long int jsrseed );
};
}

//#include "Ziggurat/Ziggurat.inlines"

