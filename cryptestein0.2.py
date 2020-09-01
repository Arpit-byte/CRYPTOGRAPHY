


def NAME():
	print("\n█▀▀ █▀▀█ █░░█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ █▀▀ ░▀░ █▀▀▄\n█░░ █▄▄▀ █▄▄█ █░░█ ░░█░░ █▀▀ ▀▀█ ░░█░░ █▀▀ ▀█▀ █░░█\n▀▀▀ ▀░▀▀ ▄▄▄█ █▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀░░▀\n\t\t\t\t\t𝐓𝐲𝐩𝐞 'Exit' 𝐭𝐨 𝐠𝐞𝐭 𝐨𝐮𝐭 𝐨𝐟 𝐂𝐑𝐘𝐏𝐓𝐄𝐒𝐓𝐄𝐈𝐍\n");




import sys
from os import system, name
def clear(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear')




clear();




print("\n█▀▀ █▀▀█ █░░█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ █▀▀ ░▀░ █▀▀▄\n█░░ █▄▄▀ █▄▄█ █░░█ ░░█░░ █▀▀ ▀▀█ ░░█░░ █▀▀ ▀█▀ █░░█\n▀▀▀ ▀░▀▀ ▄▄▄█ █▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀░░▀\n\t\t\t\t\t𝐓𝐲𝐩𝐞 '𝐄xit' 𝐭𝐨 𝐠𝐞𝐭 𝐨𝐮𝐭 𝐨𝐟 𝐂𝐑𝐘𝐏𝐓𝐄𝐒𝐓𝐄𝐈𝐍\n");





def exit():
	

	clear();
	print("Have a Good Day");
	sys.exit();



def Cryptestein():

	try:
		

		cryptestein=input("Enter 'A' to perform Additive Cipher\nEnter 'M' to perform Multiplicative Cipher\nEnter 'AK' to perform Autokey Cipher\nEnter 'RSA' to perform RSA Algorithm\nSo what's on your mind :  ");
		

		
		
		if cryptestein=='A':


			

			clear();


			

			NAME();


			

			def Crypt():

				try:


					

					crypt=input("Enter 'E' for Encryption\nEnter 'D' for Decryption\nEnter 'B' for Brute force the key\nSo what's on your mind : ");



					if crypt=='E':
			
						

						clear();


						

						NAME();


			
						print("\nEncryption Starting\n");


						

						def Encryption():	


							try:


						

								str=input("Enter the Text you want to Encrypt in Small Alphabets Anly : ");



						

								clear();


						

								NAME();


						

								if str=="Exit":

									exit();


						

								char=False;					
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]
								for c in str:

									if c.isdigit() or c.isupper():

										char=True;
									
									elif c==chr(92):
											char=True;
						
									else:
										for i in ls:
											if i==c:

												char=True;


						

								if char==True:

									print("\nYou do not enter the Text in Lowercase Letters or you entered Number along with the Text or you entered Special Symbols along with Text\n");


						

									Encryption();

								
						

								else:
									def K(): 
										
										try:
											key=input("\nEnter the value of key in numeric characters only and between 0 to 25 without Special Characters : ");


						

											clear();


						

											NAME();


						

											if key=="Exit":
												exit();	


						

											k=True;

											if key.isdigit()!=True:
												k=False

											elif int(key)>25:
												k=False

											elif int(key)<0:
												k=False


						
											if k==False:
												print("You entered an alphabet along with a numeric value or you entered a special symbol along with a numeric value or you were not in the limit from 0 to 25 in entering key or you entered nothing");


						

												K();
											

						

											else:
												index=[];
												for i in str:
													if i==" ":
														index.append(32);
													else:
														index.append(ord(i)-97);
												
												encrypt_val=[];
												start=0;
												for en_val in index:
													if en_val==32:
														encrypt_val.append(32);
														start=start+1;
													else:				
														encrypt_val.append((int(index[start])+int(key))%26);
														start=start+1;
												
												encrypt_num=0;
												encrypt_word=[];
												for i in encrypt_val:
													if i==32:
														encrypt_word.append(chr(32));
													else:				
														encrypt_num=65+i;
														encrypt_word.append(chr(encrypt_num));
														encrypt_num=0;
												
												encrypted_word="";
												for encrypt_letter in encrypt_word:
													encrypted_word=encrypted_word+encrypt_letter;


												
												print("\nEncrypted text of","'"+str+"'","is","'"+encrypted_word+"'");



										except KeyboardInterrupt:

						

											clear();


						
				
											NAME();
										
											print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

											K();
									K();	


						
							except KeyboardInterrupt:

						

								clear();


						
				
								NAME();


								print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

								Encryption();


						

						Encryption();

					elif crypt=='D':
						
						

						clear();


						

						NAME();


			
						print("\nDecryption Starting\n");


						

						def Decryption():	


							try:


						

								str=input("Enter the Text you want to Decrypt in Capital Alphabets Anly : ");



						

								clear();


						

								NAME();


						

								if str=="Exit":

									exit();


						

								char=False;			
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
									
									elif c==chr(92):
											char=True;
						
									else:
										for i in ls:
											if i==c:

												char=True;


								if char==True:

									print("\nYou do not enter the Text in Lowercase Letters or you entered Number along with the Text or you entered Special Symbols along with Text\n");


						

									Decryption();

								
						

								else:
									def K(): 
										
										try:
											key=input("\nEnter the value of key in numeric characters only and between 0 to 25 without Special Characters : ");


						

											clear();


						

											NAME();


						

											if key=="Exit":
												exit();	


						

											k=True;

											if key.isdigit()!=True:
												k=False

											elif int(key)>25:
												k=False

											elif int(key)<0:
												k=False


						
											if k==False:
												print("You entered an alphabet along with a numeric value or you entered a special symbol along with a numeric value or you were not in the limit from 0 to 25 in entering key or you entered nothing");


						

												K();
											

						
											
											else:
												index=[];
												for i in str:
													if i==" ":
														index.append(32);
													else:
														index.append(ord(i)-65);
											
												decrypt_val=[];
												start=0;
												for den_val in index:
													if den_val==32:
														decrypt_val.append(32);
														start=start+1;
													else:				
														a=int(index[start])-int(key);
														if a<0:
															a=a+26;
															m=a%26;
															decrypt_val.append(m);
															start=start+1;
														else:
															m=a%26;
															decrypt_val.append(m);
															start=start+1;
												
												decrypt_num=0;
												decrypt_word=[];
												for i in decrypt_val:
													if i==32:
														decrypt_word.append(chr(32));
													else:				
														decrypt_num=97+i;
														decrypt_word.append(chr(decrypt_num));
														decrypt_num=0;
												
												decrypted_word="";
												for decrypt_letter in decrypt_word:
													decrypted_word=decrypted_word+decrypt_letter;
												
												print("\nDecrypted text of","'"+str+"'","is","'"+decrypted_word+"'");



										except KeyboardInterrupt:

						

											clear();


						
				
											NAME();
										
											print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

											K();
									K();	


						
							except KeyboardInterrupt:

						

								clear();


						
				
								NAME();


								print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

								Decryption();


						

						Decryption();
					

					elif crypt=='B':
						
						

						clear();


						

						NAME();


			
						print("\nBruteForce Starting\n");
						

						def Brute():
							
							
							try:


								str=input("Enter the text you want to decrypt in capital alphabets only without special symbols : ");
								if str=="Exit":
									exit();
								
								if str=="":
									clear();


						

									NAME();

									print("You did not entered anything and pressed enter");
									Brute();
								char=False;			
								
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
									
									elif c==chr(92):
											char=True;
						
									else:
										for i in ls:
											if i==c:

												char=True;


								if char==True:
									clear();
		
									NAME();

									print("\nYou do not enter the Text in Lowercase Letters or you entered Number along with the Text or you entered Special Symbols along with Text\n");

									Brute();

								else:
									clear();
		
									NAME();


									index=[];
									for i in str:
										if i==" ":
											index.append(32);
										else:
											index.append(ord(i)-65);
											
									decrypt_val=[];
									start=0;
									for key in range(0,26):
										for den_val in index:

											if den_val==32:
												decrypt_val.append(32);
												start=start+1;

											else:
												a=int(index[start])-int(key);
												if a<0:
													a=a+26;
													m=a%26;
													decrypt_val.append(m);
													start=start+1;

												else:
													m=a%26;
													decrypt_val.append(m);
													start=start+1;
												
											decrypt_num=0;
											decrypt_word=[];
											for i in decrypt_val:
												if i==32:
													decrypt_word.append(chr(32));		
												else:				
													decrypt_num=97+i;
													decrypt_word.append(chr(decrypt_num));
													decrypt_num=0;
												
											decrypted_word="";
											for decrypt_letter in decrypt_word:
												decrypted_word=decrypted_word+decrypt_letter;


										print("Key =",key,"\t\t","text =",decrypted_word);
										decrypt_val=[];
										start=0;

							except KeyboardInterrupt:

						

								clear();


						
				
								NAME();


								print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

								Brute();	


						Brute();

					elif crypt=="Exit":
						exit();

					else:

						

						clear();


						
					
						NAME();
					

						
						
						print("You entered another character instead of 'B', 'E' or 'D'");


						
						Crypt();

				except KeyboardInterrupt:

					

					clear();


					
				
					NAME();


					

					print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");
					Crypt();


			
			Crypt();
		elif cryptestein=='M':
			clear();


			

			NAME();

			def Cyber():
				try:
					print("\n");
					cyber=input("Enter 'E' for Encryption\nEnter 'D' for Decryption\nEnter 'B' for Brute force the key\nSo what's on your mind : ");

					if cyber=='E':
						clear();


						

						NAME();
						print("\nEncryption Starting\n");
						def Encryption():	
							try:
								str=input("Enter the Text you want to Encrypt in Small Alphabets Anly : ");
								clear();


						

								NAME();
								if str=="Exit":

									exit();

								char=False;			
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]

								for c in str:

									if c.isdigit() or c.isupper():

										char=True;
									
									elif c==chr(92):
											char=True;
						
									else:
										for i in ls:
											if i==c:

												char=True;

								if char==True:
									print("\nYou do not enter the Text in Lowercase Letters or you entered Number along with the Text or you entered Special Symbols along with Text\n");
									Encryption();

								else:
									def K():
										try: 
											key=input("\nEnter the value of key in numeric characters only and between 0 to 25 without Special Characters : ");
											clear();


						

											NAME();


						

											if key=="Exit":
												exit();	
											
											k=True;
											if key.isdigit()!=True:
												k=False
											elif int(key)>25:
												k=False
											elif int(key)<0:
												k=False

											if k==False:
												print("You entered an alphabet along with a numeric value or you entered a special symbol along with a numeric value or you were not in the limit from 0 to 25 in entering key or you entered nothing");
												K();
											
											else:
												index=[];
												for i in str:
													if i==" ":
														index.append(32);
													else:
														index.append(ord(i)-97);
												
												encrypt_val=[];
												start=0;
												for en_val in index:
													if en_val==32:
														encrypt_val.append(32);
														start=start+1;
													else:				
														encrypt_val.append((int(index[start])*int(key))%26);
														start=start+1;
												
												encrypt_num=0;
												encrypt_word=[];
												for i in encrypt_val:
													if i==32:
														encrypt_word.append(chr(32));
													else:				
														encrypt_num=65+i;
														encrypt_word.append(chr(encrypt_num));
														encrypt_num=0;
												
												encrypted_word="";
												for encrypt_letter in encrypt_word:
													encrypted_word=encrypted_word+encrypt_letter;
												
												print("\nEncrypted text of","'"+str+"'","is","'"+encrypted_word+"'");
										except KeyboardInterrupt:

						

											clear();


						
				
											NAME();
										
											print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

											K();

									K();
							except KeyboardInterrupt:

						

								clear();


						
				
								NAME();


								print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

								Encryption();

						Encryption();

					elif cyber=='D':
						clear();


						

						NAME();

						print("\nDecryption Starting\n");
						def Decryption():
							try:	
								str=input("Enter the Text you want to Decrypt in Capital Alphabets only without Special Symbols: ");
								clear();


						

								NAME();


						

								if str=="Exit":

									exit();

								char=False;
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
									
									elif c==chr(92):
											char=True;
						
									else:
										for i in ls:
											if i==c:

												char=True;
								
								if char==True:
									print("\nYou do not enter the Text in Uppercase letters or you entered number along with the Text or you entered the Text with Special Symbols\n");
									Decryption();

								else:
									def K():
										try:
											k=True; 
											key=input("\nEnter the value of key in numeric characters only and between 0 to 25 without Special Characters : ");
											clear();


						

											NAME();
											if key=="Exit":
												exit();	

											if key.isdigit()!=True:
												k=False
											elif int(key)>25:
												k=False
											elif int(key)<0:
												k=False

											if k==False:
												print("You entered an alphabet along with a numeric value or you entered a Special Symbol along with key or you entered nothing");
												K();
											else:
												index=[];
												for i in str:
													if i==" ":
														index.append(32);
													else:
														index.append(ord(i)-65);
												
												if int(key)>26:
													smaller=26;
												
												else:
													smaller=int(key);
												for i in range(1,smaller+1):

													if((int(key)%i==0)and(26%i==0)):
														gcd=i;
												if gcd==1:
													print("multiplicative inverse exists");
													t1=0;
													t2=1;
													r2=int(key); 
													r1=26

													while r2!=0:
														q=r1//r2;
														r=r1%r2;
														t=t1-(q*t2);
														r1=r2;
														r2=r;
														t1=t2;
														t2=t;
													if t1<0:
														t1=t1+26;

													decrypt_val=[];
													start=0;
													for den_val in index:
														if den_val==32:
															decrypt_val.append(32);
															start=start+1;
														else:				
															a=int(index[start])*int(t1);
															if a<0:
																a=a+26;
																m=a%26;
																decrypt_val.append(m);
																start=start+1;
															else:
																m=a%26;
																decrypt_val.append(m);
																start=start+1;
												
													decrypt_num=0;
													decrypt_word=[];
													for i in decrypt_val:
														if i==32:
															decrypt_word.append(chr(32));
														else:				
															decrypt_num=97+i;
															decrypt_word.append(chr(decrypt_num));
															decrypt_num=0;
												
													decrypted_word="";
													for decrypt_letter in decrypt_word:
														decrypted_word=decrypted_word+decrypt_letter;
												
													print("\nDecrypted text of","'"+str+"'","is","'"+decrypted_word+"'");
												else:
													print("Multiplicative Inverse does not exists at key=",key);
													K();
										except KeyboardInterrupt:

						

											clear();


						
				
											NAME();
										
											print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

											K();
									K();
							except KeyboardInterrupt:

						

								clear();


						
				
								NAME();


								print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

								Decryption();

						Decryption();

					elif cyber=='B':
						clear();


						

						NAME();

						print("\nBruteForce Starting\n");
						def Brute():
							try:
								str=input("Enter the text you want to decrypt in capital alphabets only without special symbols : ");
								if str=="Exit":
									exit();
								
								if str=="":
									print("You did not entered anything and pressed enter");
									Brute();

								char=False;
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
									
									elif c==chr(92):
											char=True;
						
									else:
										for i in ls:
											if i==c:

												char=True;
							
								if char==True or str=="":
									clear();
		
									NAME();

									print("\nYou do not enter the message in Uppercase letters or you entered number along with the Text or you entered the Text with Special Symbols\n");
									Brute();
									
								else:
									clear();
		
									NAME();

									index=[];
									for i in str:
										if i==" ":
											index.append(32);
										else:
											index.append(ord(i)-65);
									for key in range(1,26):		
										if key>26:
											smaller=26;
										
										else:
											smaller=key;
										for i in range(1,smaller+1):

											if((key%i==0)and(26%i==0)):
												gcd=i;
										if gcd==1:
											t1=0;
											t2=1;
											r2=int(key);
											r1=26

											while r2!=0:
												q=r1//r2;
												r=r1%r2;
												t=t1-(q*t2);
												r1=r2;
												r2=r;
												t1=t2;
												t2=t;
											if t1<0:
												t1=t1+26;	
											
											decrypt_val=[];
											start=0;
											for den_val in index:

												if den_val==32:
													decrypt_val.append(32);
													start=start+1;

												else:
													a=int(index[start])*int(key);
													if a<0:
														a=a+26;
														m=a%26;
														decrypt_val.append(m);
														start=start+1;

													else:
														m=a%26;
														decrypt_val.append(m);
														start=start+1;
														
												decrypt_num=0;
												decrypt_word=[];
												for i in decrypt_val:
													if i==32:
														decrypt_word.append(chr(32));
													else:				
														decrypt_num=97+i;
														decrypt_word.append(chr(decrypt_num));
														decrypt_num=0;
														
												decrypted_word="";
												for decrypt_letter in decrypt_word:
													decrypted_word=decrypted_word+decrypt_letter;
														
											print("Key =",t1,"\t\t","text =",decrypted_word);
											decrypt_val=[];
											start=0;
							except KeyboardInterrupt:

						

								clear();


						
				
								NAME();


								print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

								Brute();	

						Brute();
					elif cyber=="Exit":
						exit();

					else:
						clear();


						
					
						NAME();

						print("You entered another character instead of 'B', 'E' or 'D'");
						Cyber();


				except KeyboardInterrupt:

					

					clear();


					
				
					NAME();


					

					print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");
					Cyber();
			Cyber();


		elif cryptestein=='AK':


			

			clear();


			

			NAME();


			

			def Autokey():

				try:


						

					autokey=input("Enter 'E' for Encryption\nEnter 'D' for Decryption\nEnter 'B' for Brute force the key\nSo what's on your mind : ");



					if autokey=='E':
				
							

						clear();


							

						NAME();


				
						print("\nEncryption Starting\n");


							

						def Encryption():	


							try:


							

								str=input("Enter the Text you want to Encrypt in Small Alphabets Anly : ");



							

								clear();


							

								NAME();


							

								if str=="Exit":

									exit();


							

								char=False;					
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]
								for c in str:

									if c.isdigit() or c.isupper():

										char=True;
									
									elif c==chr(92):
											char=True;
							
									else:
										for i in ls:
											if i==c:

												char=True;


							

								if char==True:

									print("\nYou do not enter the Text in Lowercase Letters or you entered Number along with the Text or you entered Special Symbols along with Text\n");


							

									Encryption();

									
							

								else:
									def K(): 
										
										try:
											key=input("\nEnter the value of key in numeric characters only and between 0 to 25 without Special Characters : ");

							

											clear();


							

											NAME();


							

											if key=="Exit":
												exit();	

							

											k=True;

											if key.isdigit()!=True:
												k=False

											elif int(key)>25:
												k=False

											elif int(key)<0:
												k=False


							
											if k==False:
												print("You entered an alphabet along with a numeric value or you entered a special symbol along with a numeric value or you were not in the limit from 0 to 25 in entering key or you entered nothing");


							

												K();
												

							

											else:
												index=[];
												space=[i for i in range(len(str)) if str[i]==" "];
												for i in str:
													if i==" ":
														pass;
													else:
														index.append(ord(i)-97);
													
												key_list=[int(key)];
												for i in index:
													key_list.append(i);

												encrypt_val=[];
												start=0;
												for en_val in index:
													encrypt_val.append((int(index[start])+key_list[start])%26);
													start=start+1;
												
												encrypt_num=0;
												encrypt_word=[];
												for i in encrypt_val:
													encrypt_num=65+i;
													encrypt_word.append(chr(encrypt_num));
													encrypt_num=0;

												for i in space:
													encrypt_word.insert(i," ");

												encrypted_word="";
												for encrypt_letter in encrypt_word:
													encrypted_word=encrypted_word+encrypt_letter;


													
												print("\nEncrypted text of","'"+str+"'","is","'"+encrypted_word+"'");


										except KeyboardInterrupt:

							

											clear();


							
					
											NAME();
											
											print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


							

											K();
									K();	


							
							except KeyboardInterrupt:

							

								clear();


							
					
								NAME();

								print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


							

								Encryption();


							

						Encryption();

					elif autokey=='D':
						
						

						clear();


						

						NAME();


			
						print("\nDecryption Starting\n");


						

						def Decryption():	


							try:


						

								str=input("Enter the Text you want to Decrypt in Capital Alphabets Anly : ");



						

								clear();


						

								NAME();


						

								if str=="Exit":

									exit();


						

								char=False;			
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
									
									elif c==chr(92):
											char=True;
						
									else:
										for i in ls:
											if i==c:

												char=True;


								if char==True:

									print("\nYou do not enter the Text in Lowercase Letters or you entered Number along with the Text or you entered Special Symbols along with Text\n");


						

									Decryption();

								
						

								else:
									def K(): 
										
										try:
											key=input("\nEnter the value of key in numeric characters only and between 0 to 25 without Special Characters : ");


						

											clear();


						

											NAME();


						

											if key=="Exit":
												exit();	


						

											k=True;

											if key.isdigit()!=True:
												k=False

											elif int(key)>25:
												k=False

											elif int(key)<0:
												k=False


						
											if k==False:
												print("You entered an alphabet along with a numeric value or you entered a special symbol along with a numeric value or you were not in the limit from 0 to 25 in entering key or you entered nothing");


						

												K();
											

						
											
											else:
												index=[];
												space=[i for i in range(len(str)) if str[i]==" "];

												for i in str:
													if i==" ":
														pass;
													else:
														index.append(ord(i)-65);

												key_list=[int(key)];
												for i in index:
													key=i-int(key);
													if key<0:
														key=26+key;
														key_list.append(key);
													else:
														key_list.append(key);

												decrypt_val=[];
												start=0;
												for den_val in index:
													a=int(index[start])-key_list[start];
													if a<0:
														a=a+26;
														m=a%26;
														decrypt_val.append(m);
														start=start+1;
													else:
														m=a%26;
														decrypt_val.append(m);
														start=start+1;
												
												decrypt_num=0;
												decrypt_word=[];
												for i in decrypt_val:
													decrypt_num=97+i;
													decrypt_word.append(chr(decrypt_num));
													decrypt_num=0;

												for i in space:
													decrypt_word.insert(i," ");
												
												decrypted_word="";
												for decrypt_letter in decrypt_word:
													decrypted_word=decrypted_word+decrypt_letter;
												
												print("\nDecrypted text of","'"+str+"'","is","'"+decrypted_word+"'");



										except KeyboardInterrupt:

						

											clear();


						
				
											NAME();
										
											print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

											K();
									K();	


						
							except KeyboardInterrupt:

						

								clear();


						
				
								NAME();


								print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

								Decryption();


						

						Decryption();
					

					elif autokey=='B':
						
						

						clear();


						

						NAME();


			
						print("\nBruteForce Starting\n");
						

						def Brute():
							
							
							try:


								str=input("Enter the text you want to decrypt in capital alphabets only without special symbols : ");
								if str=="Exit":
									exit();
									

								char=False;			
								
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
									
									elif c==chr(92):
											char=True;
						
									else:
										for i in ls:
											if i==c:

												char=True;


								if char==True or str=="":
									clear();
		
									NAME();

									print("\nYou do not enter the Text in Lowercase Letters or you entered Number along with the Text or you entered Special Symbols along with Text\n");

									Brute();

								else:
									clear();
		
									NAME();


									index=[];
									space=[i for i in range(len(str)) if str[i]==" "];

									for i in str:
										if i==" ":
											pass;
										else:
											index.append(ord(i)-65);
											
									decrypt_val=[];
									start=0;
			
									for key in range(0,26):
										key_list=[int(key)];
										ky=key;
										for i in index:
											key=i-int(key);
											if key<0:
												key=26+key;
												key_list.append(key);
											else:
												key_list.append(key);
										for den_val in index:

											a=int(index[start])-key_list[start];
											if a<0:
												a=a+26;
												m=a%26;
												decrypt_val.append(m);
												start=start+1;

											else:
												m=a%26;
												decrypt_val.append(m);
												start=start+1;
												
											decrypt_num=0;
											decrypt_word=[];
											for i in decrypt_val:
												decrypt_num=97+i;
												decrypt_word.append(chr(decrypt_num));
												decrypt_num=0;

											for i in space:
												decrypt_word.insert(i," ");
												
											decrypted_word="";
											for decrypt_letter in decrypt_word:
												decrypted_word=decrypted_word+decrypt_letter;


										print("Key =",ky,"\t\t","text =",decrypted_word);
										decrypt_val=[];
										start=0;

							except KeyboardInterrupt:

						

								clear();


						
				
								NAME();


								print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


						

								Brute();	


						Brute();

					elif autokey=="Exit":
						exit();

					else:

						

						clear();


						
					
						NAME();
					

						
						
						print("You entered another character instead of 'B', 'E' or 'D'");


						
						Autokey();

				except KeyboardInterrupt:

					

					clear();


					
				
					NAME();


					

					print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");
					Crypt();


			
			Autokey();

		elif cryptestein=='RSA':


			

			clear();


			

			NAME();


			

			def RSA():

				try:


					

					Rsa=input("Enter 'KEY' if you want to find out Public Key or Private Key\nEnter 'CRYPTOGRAPHY' to Encrypt or Decrypt the Plain or Encrypted text\nSo what's on your mind : ");

					
					if Rsa=='KEY':

						clear();


							

						NAME();


				
						print("\nKey Starting\n");
					
						def Prime1():

							try:
							
								prime1=input("Enter First Prime Number : ");
								clear();


								

								NAME();


								

								if prime1=="Exit":

									exit();
					
								if prime1=="":
									print("\nYou did not entered anything and pressed enter\n");
									Prime1();
								char=False;
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~"," ","+",";",":",".","=","-","`",",","]"]								

								for c in prime1:

									if c.isalpha():

										char=True;
									
									elif c==chr(92):
											char=True;
						
									else:
										for i in ls:
											if i==c:

												char=True;
								
								if char==True:
									print("\nYou do not entered character along with prime number or you entered the Text with Special Symbols or you entered a negative number\n");
									Prime1();
								else:
									if int(prime1)>1:
										
										for i in range(2,int(prime1)):

											if int(prime1)%i==0:
												print("\nYou entered a non prime number\n");
												Prime1();
												break;

										else:

											def Prime2():

												try:

													prime2=input("Enter Second Prime Number which is different from first prime number you entered : ");

													clear();


											

													NAME();


											

													if prime2=="Exit":

														exit();

													if prime2=="":
														print("\nYou did not entered anything and pressed enter\n");
														Prime2();


													char=False;
													ls=["[","@","_","!","#","$","%","^","&","*","(",")"," ","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

													for c in prime2:

														if c.isalpha():

															char=True;
										
														elif c==chr(92):
															char=True;
							
														else:
															for i in ls:
																if i==c:

																	char=True;
									
													if char==True:
														print("\nYou do not entered character along with prime number or you entered the Text with Special Symbols or you entered a negative number\n");
														Prime2();

													if int(prime2)!=int(prime1):

														if int(prime2)>1:
															for i in range(2,int(prime2)):

																if int(prime2)%i==0:
																	print("\nYou entered a non prime number\n");
																	Prime2();

															else:

																n=int(prime1)*int(prime2);

																phie_n=(int(prime1)-1)*(int(prime2)-1);

																def E():

																	try:

																		e=input("Enter the Value of public key which is greater than 1 and less than {} : ".format(phie_n));

																		clear();


												

																		NAME();


												

																		if e=="Exit":

																			exit();

																		if e=="":
																			print("\nYou did not entered anything and pressed enter\n");
																			E();
																		char=False;
																		ls=["[","@","_","!","#","$","%","^","&","*","(",")"," ","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

																		for c in e:

																			if c.isalpha():

																				char=True;
											
																			elif c==chr(92):
																				char=True;
								
																			else:
																				for i in ls:
																					if i==c:

																						char=True;
									
																		if char==True:
																			print("\nYou do not entered character along with prime number or you entered the Text with Special Symbols or you entered a negative number\n");
																			E();
	
																		else:
																			if int(e)>1 and int(e)<phie_n:
																				if int(e)>phie_n:
																					smaller=phie_n;

																				else:
																					smaller=int(e);

																				for i in range(1,smaller+1):
																					if (int(e) % i == 0) and (phie_n % i == 0):
																						gcd=i;
																			
																				if gcd!=1:
																					print("\nThe GCD of Public Key and phie_n is not equal to 1\n");
																					Prime1();

																				else:
															
																					i=1;
																					while True:
																						if (phie_n*i+1)%int(e)==0:
																							d=(phie_n*i+1)//int(e);
																							break;
																						else:
																							i=i+1;
																								
																					print("private key is",d);
																					sys.exit();
																			else:
																				print("\nYou did not entered the value between 1 and",phie_n,"\n");
																				E();
																	except KeyboardInterrupt:
															

																		clear();


															
										
																		NAME();


																		print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");
																		E();
																E();

														else:
															print("\nYou entered a non prime number\n");
															Prime2();
													else:
														print("\nYou entered a non prime number or the number was equal to the first prime numeber you entered\n");
														Prime2();

												except KeyboardInterrupt:
		
											

													clear();


											
									
													NAME();


													print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


											

													Prime2();
											Prime2();
									else:
										print("\nThe number you entered is not a prime number\n");	
										Prime1();
							except KeyboardInterrupt:

								
	
								clear();


								
						
								NAME();


								print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


								

								Prime1();

								

						Prime1();

					if Rsa=='CRYPTOGRAPHY':

						clear();


							

						NAME();


				
						print("\nCRYPTING\n");
					
						def Prime1():

							try:
							
								prime1=input("Enter First Prime Number : ");
								clear();


								

								NAME();


								

								if prime1=="Exit":

									exit();
					
								if prime1=="":
									print("\nYou did not entered anything and pressed enter\n");
									Prime1();
								char=False;
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~"," ","+",";",":",".","=","-","`",",","]"]								

								for c in prime1:

									if c.isalpha():

										char=True;
									
									elif c==chr(92):
											char=True;
						
									else:
										for i in ls:
											if i==c:

												char=True;
								
								if char==True:
									print("\nYou do not entered character along with prime number or you entered the Text with Special Symbols or you entered a negative number\n");
									Prime1();
								else:
									if int(prime1)>1:
										
										for i in range(2,int(prime1)):

											if int(prime1)%i==0:
												print("\nYou entered a non prime number\n");
												Prime1();
												break;

										else:

											def Prime2():

												try:

													prime2=input("Enter Second Prime Number which is different from first prime number you entered : ");

													clear();


											

													NAME();


											

													if prime2=="Exit":

														exit();

													if prime2=="":
														print("\nYou did not entered anything and pressed enter\n");
														Prime2();


													char=False;
													ls=["[","@","_","!","#","$","%","^","&","*","(",")"," ","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

													for c in prime2:

														if c.isalpha():

															char=True;
										
														elif c==chr(92):
															char=True;
							
														else:
															for i in ls:
																if i==c:

																	char=True;
									
													if char==True:
														print("\nYou do not entered character along with prime number or you entered the Text with Special Symbols or you entered a negative number\n");
														Prime2();

													if int(prime2)!=int(prime1):

														if int(prime2)>1:
															for i in range(2,int(prime2)):

																if int(prime2)%i==0:
																	print("\nYou entered a non prime number\n");
																	Prime2();

															else:

																n=int(prime1)*int(prime2);

																phie_n=(int(prime1)-1)*(int(prime2)-1);

																def E():

																	try:

																		e=input("Enter the Value of public key which is greater than 1 and less than {} : ".format(phie_n));

																		clear();


												

																		NAME();


												

																		if e=="Exit":

																			exit();

																		if e=="":
																			print("\nYou did not entered anything and pressed enter\n");
																			E();
																		char=False;
																		ls=["[","@","_","!","#","$","%","^","&","*","(",")"," ","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

																		for c in e:

																			if c.isalpha():

																				char=True;
											
																			elif c==chr(92):
																				char=True;
								
																			else:
																				for i in ls:
																					if i==c:

																						char=True;
									
																		if char==True:
																			print("\nYou do not entered character along with prime number or you entered the Text with Special Symbols or you entered a negative number\n");
																			E();
	
																		else:
																			if int(e)>1 and int(e)<phie_n:
																				if int(e)>phie_n:
																					smaller=phie_n;

																				else:
																					smaller=int(e);

																				for i in range(1,smaller+1):
																					if (int(e) % i == 0) and (phie_n % i == 0):
																						gcd=i;
																			
																				if gcd!=1:
																					print("\nThe GCD of Public Key and phie_n is not equal to 1\n");
																					Prime1();

																				else:
															
																					i=1;
																					while True:
																						if (phie_n*i+1)%int(e)==0:
																							d=(phie_n*i+1)//int(e);
																							break;
																						else:
																							i=i+1;

																					def Choice():
												
																						try:
					
																							choice=input("Enter 'E' for Encryption\nEnter 'D' for Decryption\nSo what's on your mind : ");
																							

																							if choice=='E':
			
						

																								clear();


						

																								NAME();	


			
																								print("\nEncryption Starting\n");


						

																								def Encryption():	


																									try:


						

																										str=input("Enter the Text you want to Encrypt in Small Alphabets Anly : ");



						

																										clear();


						

																										NAME();


						

																										if str=="Exit":

																											exit();

																										if str=="":
																											print("\nYou did not entered anything and pressed enter\n");
						

																										char=False;					
																										ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]
																										for c in str:

																											if c.isdigit() or c.isupper():

																												char=True;
									
																											elif c==chr(92):
																												char=True;
						
																											else:
																												for i in ls:
																													if i==c:

																														char=True;


						

																										if char==True:

																											print("\nYou do not enter the Text in Lowercase Letters or you entered Number along with the Text or you entered Special Symbols along with Text\n");


						

																											Encryption();

																										else:
						
																											index=[];
																											for i in str:
																												if i==" ":
																													index.append(32);
																												else:
																													index.append(ord(i)-97);

																											C=[];
																											for i in index:

																												if i==32:
																													C.append(int(i));

																												else:
																													c=(int(i)**int(e))%n;
																													C.append(c);

																											encrypt_word=[];
																											for i in C:
																												if i==32:
																													encrypt_word.append(chr(32));
																												else:				
																													encrypt_word.append(i);
																											
																											encrypted_word="";
																											for encrypt_letter in encrypt_word:
																												encrypted_word=encrypted_word+"{}".format(encrypt_letter)+",";
																											encrypted_word=encrypted_word[:-1];																						
																											print("\nEncrypted text of","'"+str+"'","is","'"+encrypted_word+"'");
																											sys.exit();

																									except KeyboardInterrupt:

						
																										clear();


						
				
																										NAME();


																										print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");
	

						

																										Encryption();


						

																								Encryption();


																							elif choice=='D':
			
						

																								clear();


						

																								NAME();	


			
																								print("\nDecryption Starting\n");


						

																								def Decryption():	


																									try:


						

																										str=input("Enter the Text you want to Decrypt in numbers or spaces separated with commas only : ");



						
																										clear();


						

																										NAME();


						

																										if str=="Exit":

																											exit();

																										if str=="":
																											print("\nYou did not entered anything and pressed enter\n");
						

																										char=False;					
																										ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`","]"]
																										for c in str:

																											if c.isalpha():

																												char=True;
									
																											elif c==chr(92):
																												char=True;
						
																											else:
																												for i in ls:
																													if i==c:

																														char=True;


						

																										if char==True:

																											print("\nYou entered the Text along alphabets or you entered Special Symbols along with Text\n");


						

																											Decryption();

																										else:
					
																											characters=str.split(",");
																																	
																											index=[];
																											for i in characters:
																												if i==" ":
																													index.append(32);
																												else:
																													index.append(i);

																											for i in index:
																												if i=="":
																													print("\nAt somewhere in the encrypted text, you entered consicutive commas and there was no number or space between them\n");
																													Decryption();
																											M=[];
																											for i in index:

																												if i==32:
																													M.append(int(i));

																												else:
																													m=(int(i)**int(d))%n;
																													M.append(m);
																						
																											decrypt_num=0;
																											decrypt_word=[];
																											for i in M:
																												if i==32:
																													decrypt_word.append(chr(32));
																												else:				
																													decrypt_num=97+i;
																													decrypt_word.append(chr(decrypt_num));
																													decrypt_num=0;
																											
																											decrypted_word="";
																											for decrypt_letter in decrypt_word:
																												decrypted_word=decrypted_word+decrypt_letter;																			
																											print("\nDecrypted text of","'"+str+"'","is","'"+decrypted_word+"'");
																											sys.exit();

																									except KeyboardInterrupt:

						
																										clear();


						
				
																										NAME();


																										print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");
	

						

																										Decryption();


						

																								Decryption();
																					
																							elif choice=="Exit":
																								exit();
			
		
																							else:

			

																								clear();


			
				
																								NAME();
				

			
				
																								print("You entered another character instead of 'E' or 'D'");


				
	
																								Choice();
																						
																						except KeyboardInterrupt:

						
																							clear();

						
				
																							NAME();


																							print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");
	

						

																							Choice();
						
																					Choice();		 																																																																	
																			else:
																				print("\nYou did not entered the value between 1 and",phie_n,"\n");
																				E();



																	except KeyboardInterrupt:
															

																		clear();


															
										
																		NAME();


																		print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");
																		E();
																E();

														else:
															print("\nYou entered a non prime number\n");
															Prime2();
													else:
														print("\nYou entered a non prime number or the number was equal to the first prime numeber you entered\n");
														Prime2();

												except KeyboardInterrupt:
		
											

													clear();


											
									
													NAME();


													print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


											

													Prime2();
											Prime2();
									else:
										print("\nThe number you entered is not a prime number\n");	
										Prime1();
							except KeyboardInterrupt:

								
	
								clear();


								
						
								NAME();


								print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");


								

								Prime1();

								

						Prime1();

					elif Rsa=="Exit":
						exit();

					else:

								

						clear();


								
							
						NAME();
							

								
								
						print("You entered another character instead of 'KEY' or 'CRYPTOGRAPHY'");


								
						RSA();

				except KeyboardInterrupt:

							

					clear();


							
						
					NAME();


							

					print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");
					RSA();


					
			RSA();

		elif cryptestein=="Exit":
			exit();
			
		
		else:

			

			clear();


			
				
			NAME();
				

			
				
			print("You entered another character instead of 'A' or 'M'");


			

			Cryptestein();


	

	except KeyboardInterrupt:

		

		clear();


		
				
		NAME();


		

		print("\nYou Interrupted the Working of the Program, If you want to Exit the program type 'Exit'");
		Cryptestein();




Cryptestein();
