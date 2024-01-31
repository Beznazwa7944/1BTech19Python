#include <stdio.h>
#include <math.h>

void
DecToBin (int n)
{
  char binr[12];
  int ptg;
  while (ptg < 13)
	{
	  if (n < pow (2, ptg))
		{
		  
		  break;
		}
	  ptg++;
	  printf ("PTG IS EQU TO %d\n", ptg);
	}
  printf ("CHCKPT 1 %d", ptg);
  for (int a = ptg; a > -1; a--)
	{
	  if (n - pow (2, ptg) > -1)
		{
		  n = n - pow (2, ptg);
		  binr[a] = '1';
		  printf ("ELEMENT OF ARR AT POS %d, IS EQU TO %c", a, binr[a]);
		  continue;
		}
	  else
		{
		  binr[a] = '0';
		  ("ELEMENT OF ARR AT POS %d, IS EQU TO %c", a, binr[a]);
		}

	}
  for (int a = 0; a < ptg + 1; a++)
	{
	  printf (binr[a]);
	}
}

int
main ()
{
  int inp;
  while (1 == 1)
	{
	  scanf ("%d", &inp);
	  if (inp >= 1 && inp <= 2000)
		{
		  break;
		}
	  printf ("ILLEGAL NUMBER\n");
	}
  DecToBin (inp);
}
