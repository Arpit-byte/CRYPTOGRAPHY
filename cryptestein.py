


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
		

		cryptestein=input("Enter 'A' to perform Additive Cipher\nEnter 'M' to perform Multiplicative Cipher\nSo what's on your mind :  ");
		

		
		
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
								if str=='':
									char=True;
								
								if char==True:
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
