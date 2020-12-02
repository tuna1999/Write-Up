#include <iostream>
#include <cstring>
#include <string>

using namespace std;

unsigned char sbox[256];

void RC4(char * cipher, char * flag, int size)
{
	unsigned char indexA = 0;
	unsigned char indexB = 0;
	for(int i = 0; i < size;++i)
	{
		indexA = (indexA + 1) % 256;
		indexB = (sbox[indexA] + indexB) % 256;
		swap(sbox[indexA],sbox[indexB]);
		flag[i] = cipher[i] ^ sbox[(sbox[indexA] + sbox[indexB])%256];
	}
}


void KSA(char * key,int sizeKey)
{
	int j = 0;
	for(int i = 0;i<256;++i)
		sbox[i] = i;
	for(int i = 0;i<256;++i)
	{
		j = (j + sbox[i] + key[i % sizeKey]) % 256;
		swap(sbox[i],sbox[j]);
	}
}


int main()
{
	char *cipher = (char*)"\xAD\x29\xA9\x8C\x28\x69\x72\xB0\xB4\xE8\x83\xA4\xEE\x23\xBE\xB5\x94\x94\x19\x4A\x8C\x30\x19\x29";
	char key[6];
	char flag[26];
	memset(key,0,sizeof(key));
	memset(flag,0,sizeof(flag));
	for(char i = 32;i<127;++i)
		for(char j = 32;j<127;++j)
			for(char k = 32;k<127;++k)
				for(char l = 32;l<127;++l)
				{
					key[0] = i;
					key[1] = j;
					key[2] = k;
					key[3] = l;

					KSA(key,4);
					RC4(cipher,flag,24);
					if (strstr(flag,"ASCI") == flag)
					{
						cout << key << endl;
						cout << flag << endl;
					}	 	
				}

	return 0;
}

// ASCIS{4_s1mpl3_pr0toco1}