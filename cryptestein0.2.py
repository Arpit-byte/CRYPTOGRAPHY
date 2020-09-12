


def NAME():
	print("\n█▀▀ █▀▀█ █░░█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ █▀▀ ░▀░ █▀▀▄\n█░░ █▄▄▀ █▄▄█ █░░█ ░░█░░ █▀▀ ▀▀█ ░░█░░ █▀▀ ▀█▀ █░░█\n▀▀▀ ▀░▀▀ ▄▄▄█ █▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀░░▀\n\t\t\t\t\t𝓟𝓸𝔀𝓮𝓻𝓮𝓭 𝓫𝔂 Ϛì×Ƒìղցմɾҽ\n");




import sys
from os import system, name
def clear(): 

	if name == 'nt': 
		_ = system('cls') 

	else: 
		_ = system('clear')




clear();




print("\n█▀▀ █▀▀█ █░░█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ █▀▀ ░▀░ █▀▀▄\n█░░ █▄▄▀ █▄▄█ █░░█ ░░█░░ █▀▀ ▀▀█ ░░█░░ █▀▀ ▀█▀ █░░█\n▀▀▀ ▀░▀▀ ▄▄▄█ █▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀░░▀\n\t\t\t\t\t𝓟𝓸𝔀𝓮𝓻𝓮𝓭 𝓫𝔂 Ϛì×Ƒìղցմɾҽ\n");





def exit():
	

	clear();
	print("ٱلْحَمْدُ لِلَّٰهِ");
	sys.exit();

def encryption_name():
	print("𝑬𝒏𝒄𝒓𝒚𝒑𝒕𝒊𝒐𝒏\n");	

def decryption_name():
	print("𝑫𝒆𝒄𝒓𝒚𝒑𝒕𝒊𝒐𝒏\n");	

def encryption_decryption_name():
	print("𝑬𝒏𝒄𝒓𝒚𝒑𝒕𝒊𝒐𝒏 / 𝑫𝒆𝒄𝒓𝒚𝒑𝒕𝒊𝒐𝒏\n");

def brute_name():
	print("𝑩𝒓𝒖𝒕𝒆 𝑭𝒐𝒓𝒄𝒆\n");

def key_name():
	print("𝑷𝒓𝒊𝒗𝒂𝒕𝒆 𝑲𝒆𝒚\n");

def Cryptestein():

	try:
		
		cryptestein=input("① Additive Cipher\n\n② Multiplicative Cipher\n\n③ Autokey Cipher\n\n④ RSA Algorithm\n\n⑤ Exit\n\nChoose an Option : ");
		

		
		
		if cryptestein=='1':


			

			clear();


			

			NAME();


			def additive_name():
				print("𝐀𝐝𝐝𝐢𝐭𝐢𝐯𝐞 𝐂𝐢𝐩𝐡𝐞𝐫\n")
			additive_name()	


			def Crypt():
				
				try:


					

					crypt=input("① Encryption\n\n② Decryption\n\n③ Brute Force\n\n④ Back\n\n⑤ Exit\n\nChoose an Option : ");



					if crypt=='1':
			
						

						clear();


						

						NAME();

						additive_name();

						encryption_name();

						def Encryption():	


							try:


						

								str=input("Enter the Text you want to Encrypt in Small Alphabets Only : \n\n① Back\n\n② Exit"+"\033[A"*4+"\033[C"*55);



						

								clear();


						

								NAME();

								additive_name();

								encryption_name();

								def text():
									print("𝓟𝓵𝓪𝓲𝓷 𝓣𝓮𝔁𝓽 : "+'"'+str+'"\n'); 
								text();

								if str=="1":

									clear();


						

									NAME();

									additive_name();
									Crypt();


								elif str=="2":

									exit();

								elif str=="":

									print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");

									Encryption();

						

								char=False;					
								ls=["[","@",";","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]
								for c in str:

									if c.isdigit() or c.isupper():

										char=True;
										break;
									elif c==chr(92):
											char=True;
											break;
									else:
										for i in ls:
											if i==c:

												char=True;
												break;


								if char==True:

									print("You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n");


						

									Encryption();

							

								else:
									def K(): 
										
										try:
											key=input("Enter the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters : \n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*91);


						

											clear();


						

											NAME();


											additive_name();

											encryption_name();
			
											text();
											
											def key_name():
												print("𝓚𝓮𝔂 : "+'"'+key+'"\n');
											key_name();

											if key=="A":
												
												clear();


										

												NAME();

												additive_name();
	
												encryption_name();

												Encryption();

											elif key=="B":
												exit();	

											elif key=="":

												print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");

												K();

						

											k=True;

											if key.isdigit()!=True:
												k=False

											elif int(key)>25:
												k=False

											elif int(key)<0:
												k=False


						
											if k==False:

												print("You did not Follow the Instructions and Entered",'"'+key+'",',"which contains unacceptable characters\n");


						

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


												
												print("𝓔𝓷𝓬𝓻𝔂𝓹𝓽𝓮𝓭 𝓣𝓮𝔁𝓽 : "+'"'+encrypted_word+'"\n');

												def User():

													try:
														user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
														
														if user=="1":
															clear();
															NAME();
															Cryptestein();
													
														elif user=="2":
															exit();
														
														elif user=="":
															print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
															clear();
															NAME();
															User();
						
														else:
															print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
															clear();
															NAME();
															User();
																												
													except KeyboardInterrupt:

														clear();


														

														NAME();


											
														print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
														User();

													except EOFError:

														clear();


														

														NAME();


											
														print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
														User();
												User();
										except KeyboardInterrupt:

											clear();


											

											NAME();


								
											additive_name();

											encryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();

										except EOFError:

											clear();


											

											NAME();


								
											additive_name();

											encryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();
										
									K();	


						
							except KeyboardInterrupt:

								clear();


								

								NAME();


					
								additive_name();

								encryption_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");
								Encryption();

							except EOFError:

								clear();


								

								NAME();


					
								additive_name();

								encryption_name();	
		
								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");
								Encryption();


						

						Encryption();

					elif crypt=='2':
						
						

						clear();


						

						NAME();


			
						additive_name();

						decryption_name();


						

						def Decryption():	


							try:


						

								str=input("Enter the Text you want to Decrypt in Capital Alphabets Only : \n\n① Back\n\n② Exit"+"\033[A"*4+"\033[C"*57);



						

								clear();


						

								NAME();

								additive_name();

								decryption_name();

								def text():
									print("𝓔𝓷𝓬𝓻𝔂𝓹𝓽𝓮𝓭 𝓣𝓮𝔁𝓽 : "+'"'+str+'"\n'); 
								text();

								if str=="1":

									clear();


						

									NAME();

									additive_name();
									Crypt();


								elif str=="2":

									exit();

								elif str=="":

									print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");

									Decryption();


								char=False;			
								ls=["[","@",";","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
										break;									
									elif c==chr(92):
											char=True;
											break;
									else:
										for i in ls:
											if i==c:

												char=True;
												break;

								if char==True:

									print("You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n");


						

									Decryption();

								
						

								else:
									def K(): 
										
										try:
											key=input("Enter the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters : \n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*91);


						

											clear();


						

											NAME();


											additive_name();

											decryption_name();
			
											text();
											
											def key_name():
												print("𝓚𝓮𝔂 : "+'"'+key+'"\n');
											key_name();

											if key=="A":
												
												clear();


										

												NAME();

												additive_name();
	
												decryption_name();

												Decryption();

											elif key=="B":
												exit();	

											elif key=="":

												print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");

												K();


						

											k=True;

											if key.isdigit()!=True:
												k=False

											elif int(key)>25:
												k=False

											elif int(key)<0:
												k=False


						
											if k==False:
												print("You did not Follow the Instructions and Entered",'"'+key+'",',"which contains unacceptable characters\n");


						

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
												
												print("𝓟𝓵𝓪𝓲𝓷 𝓣𝓮𝔁𝓽 : "+'"'+decrypted_word+'"\n');

												def User():

													try:
														user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
														
														if user=="1":
															clear();
															NAME();
															Cryptestein();
													
														elif user=="2":
															exit();
														
														elif user=="":
															print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
															clear();
															NAME();
															User();
						
														else:
															print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
															clear();
															NAME();
															User();
																												
													except KeyboardInterrupt:

														clear();


														

														NAME();


											
														print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
														User();

													except EOFError:

														clear();


														

														NAME();


											
														print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
														User();
												User();



										except KeyboardInterrupt:

											clear();


											

											NAME();


								
											additive_name();

											decryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();

										except EOFError:

											clear();


											

											NAME();


								
											additive_name();

											decryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();
										
									K();	


						
							except KeyboardInterrupt:

								clear();


								

								NAME();


					
								additive_name();

								decryption_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Decryption();

							except EOFError:

								clear();


								

								NAME();


					
								additive_name();

								decryption_name();	
		
								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Decryption();


						

						Decryption();
					

					elif crypt=='3':
						
						

						clear();


						

						NAME();


			
						additive_name();

						brute_name();
						

						def Brute():
							
							
							try:


								str=input("Enter the Text you want to Decrypt in Capital Alphabets Only : \n\n① Back\n\n② Exit"+"\033[A"*4+"\033[C"*57);



						

								clear();


						

								NAME();

								additive_name();

								brute_name();

								def text():
									print("𝓔𝓷𝓬𝓻𝔂𝓹𝓽𝓮𝓭 𝓣𝓮𝔁𝓽 : "+'"'+str+'"\n'); 
								text();

								if str=="1":

									clear();


						

									NAME();

									additive_name();
									Crypt();


								elif str=="2":

									exit();

								elif str=="":

									print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");

									Brute();
								char=False;			
								
								ls=["[","@",";","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
										break;										
									elif c==chr(92):
										char=True;
										break;
									else:
										for i in ls:
											if i==c:

												char=True;
												break;

								if char==True:

									print("You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n");

									Brute();

								else:
									clear();
		
									NAME();

									additive_name();

									brute_name();
			
									text();

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


										print("𝓚𝓮𝔂 : "+'"'+"{}".format(key)+'" '+"𝓟𝓵𝓪𝓲𝓷 𝓣𝓮𝔁𝓽 : "+'"'+decrypted_word+'"\n');

										decrypt_val=[];
										start=0;
									def User():

										try:
											user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
														
											if user=="1":
												clear();
												NAME();
												Cryptestein();
													
											elif user=="2":
												exit();
														
											elif user=="":
												print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
												clear();
												NAME();
												User();
						
											else:
												print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
												clear();
												NAME();
												User();
																											
										except KeyboardInterrupt:

											clear();


														

											NAME();


											
											print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
											User();

										except EOFError:

											clear();


														

											NAME();


											
											print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
											User();
									User();

							except KeyboardInterrupt:

								clear();


								

								NAME();


					
								additive_name();

								decryption_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Brute();

							except EOFError:

								clear();


								

								NAME();


					
								additive_name();

								decryption_name();	
		
								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Brute();


						Brute();

					elif crypt=="4":

						clear();


						
					
						NAME();

						Cryptestein();

					elif crypt=="5":
						exit();


					elif crypt=="":

			

						clear();


			
				
						NAME();
				

						additive_name()	
			
				
						print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");


			

						Crypt();


					else:

						

						clear();


						
					
						NAME();
					
						additive_name()	
	
						
						
						print("You Entered",'"'+crypt+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");


						
						Crypt();

				except KeyboardInterrupt:

					

					clear();


					
				
					NAME();


					additive_name()	
					

					print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");
					Crypt();

				except EOFError:

					

					clear();


					
							
					NAME();


					additive_name()	
					

					print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");
					Crypt();

			
			Crypt();
		elif cryptestein=='2':
			clear();


			

			NAME();

			def multiplicative_name():
				print("𝐌𝐮𝐥𝐭𝐢𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐯𝐞 𝐂𝐢𝐩𝐡𝐞𝐫\n")
			multiplicative_name()	

			def Cyber():
				try:
					cyber=input("① Encryption\n\n② Decryption\n\n③ Brute Force\n\n④ Back\n\n⑤ Exit\n\nChoose an Option : ");

					if cyber=='1':
			
						

						clear();


						

						NAME();

						multiplicative_name();

						encryption_name();
						def Encryption():	
							try:
								str=input("Enter the Text you want to Encrypt in Small Alphabets Only : \n\n① Back\n\n② Exit"+"\033[A"*4+"\033[C"*55);

						

								clear();


						

								NAME();

								multiplicative_name();

								encryption_name();

								def text():
									print("𝓟𝓵𝓪𝓲𝓷 𝓣𝓮𝔁𝓽 : "+'"'+str+'"\n'); 
								text();

								if str=="1":

									clear();


						

									NAME();

									multiplicative_name();
									Cyber();


								elif str=="2":

									exit();

								elif str=="":

									print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");

									Encryption();

								char=False;			
								ls=["[","@",";","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]
								for c in str:

									if c.isdigit() or c.isupper():

										char=True;
										break;
									elif c==chr(92):
											char=True;
											break;
									else:
										for i in ls:
											if i==c:

												char=True;
												break;

								if char==True:
									print("You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n");
									Encryption();

								else:
									def K():
										try: 
											key=input("Enter the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters : \n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*91);


						

											clear();


						

											NAME();


											multiplicative_name();

											encryption_name();
			
											text();
											
											def key_name():
												print("𝓚𝓮𝔂 : "+'"'+key+'"\n');
											key_name();

						

											if key=="A":
												
												clear();


										

												NAME();

												multiplicative_name();
	
												encryption_name();

												Encryption();

											elif key=="B":
												exit();	

											elif key=="":

												print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");

												K();
											
											k=True;
											if key.isdigit()!=True:
												k=False
											elif int(key)>25:
												k=False
											elif int(key)<0:
												k=False

											if k==False:
												print("You did not Follow the Instructions and Entered",'"'+key+'",',"which contains unacceptable characters\n");
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
												
												print("𝓔𝓷𝓬𝓻𝔂𝓹𝓽𝓮𝓭 𝓣𝓮𝔁𝓽 : "+'"'+encrypted_word+'"\n');

												def User():

													try:
														user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
														
														if user=="1":
															clear();
															NAME();
															Cryptestein();
													
														elif user=="2":
															exit();
														
														elif user=="":
															print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
															clear();
															NAME();
															User();
						
														else:
															print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
															clear();
															NAME();
															User();
																												
													except KeyboardInterrupt:

														clear();


														

														NAME();


											
														print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
														User();

													except EOFError:

														clear();


														

														NAME();


											
														print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
														User();
												User();

										except KeyboardInterrupt:

											clear();


											

											NAME();


								
											multiplicative_name();

											encryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();

										except EOFError:

											clear();


											

											NAME();


								
											multiplicative_name();

											encryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();
										
									K();	


						
							except KeyboardInterrupt:

								clear();


								

								NAME();


					
								multiplicative_name();

								encryption_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");
								Encryption();

							except EOFError:

								clear();


								

								NAME();


					
								multiplicative_name();

								encryption_name();	
		
								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");
								Encryption();


						

						Encryption();

					elif cyber=='2':

						clear();


						

						NAME();


			
						multiplicative_name();

						decryption_name();

						def Decryption():
							try:
								str=input("Enter the Text you want to Decrypt in Capital Alphabets Only : \n\n① Back\n\n② Exit"+"\033[A"*4+"\033[C"*57);



						

								clear();


						

								NAME();

								multiplicative_name();

								decryption_name();

								def text():
									print("𝓔𝓷𝓬𝓻𝔂𝓹𝓽𝓮𝓭 𝓣𝓮𝔁𝓽 : "+'"'+str+'"\n'); 
								text();

						

								if str=="1":

									clear();


						

									NAME();

									multiplicative_name();
									Cyber();


								elif str=="2":

									exit();

								elif str=="":

									print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");

									Decryption();

								char=False;
								ls=["[","@",";","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
										break;									
									elif c==chr(92):
											char=True;
											break;
									else:
										for i in ls:
											if i==c:

												char=True;
												break;
								
								if char==True:
									print("You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n");
									Decryption();

								else:
									def K():
										try:
											k=True; 
											key=input("Enter the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters : \n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*91);


						

											clear();


						

											NAME();


											multiplicative_name();

											decryption_name();
			
											text();
											
											def key_name():
												print("𝓚𝓮𝔂 : "+'"'+key+'"\n');
											key_name();

											if key=="A":
												
												clear();


										

												NAME();

												multiplicative_name();
	
												decryption_name();

												Decryption();

											elif key=="B":
												exit();	

											elif key=="":

												print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");

												K();

											if key.isdigit()!=True:
												k=False
											elif int(key)>25:
												k=False
											elif int(key)<0:
												k=False

											if k==False:
												print("You did not Follow the Instructions and Entered",'"'+key+'",',"which contains unacceptable characters\n");
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
												
													print("𝓟𝓵𝓪𝓲𝓷 𝓣𝓮𝔁𝓽 : "+'"'+decrypted_word+'"\n');
													def User():

														try:
															user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
															
															if user=="1":
																clear();
																NAME();
																Cryptestein();
														
															elif user=="2":
																exit();
															
															elif user=="":
																print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
																clear();
																NAME();
																User();
							
															else:
																print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
																clear();
																NAME();
																User();
																													
														except KeyboardInterrupt:

															clear();


															

															NAME();


												
															print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
															User();

														except EOFError:

															clear();


															

															NAME();


												
															print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
															User();
													User();

												else:
													print("Multiplicative Inverse does not exists at key=",key);
													K();

										except KeyboardInterrupt:

											clear();


											

											NAME();


								
											multiplicative_name();

											decryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();

										except EOFError:

											clear();


											

											NAME();


								
											multiplicative_name();

											decryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();
										
									K();	


						
							except KeyboardInterrupt:

								clear();


								

								NAME();


					
								multiplicative_name();

								decryption_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Decryption();

							except EOFError:

								clear();


								

								NAME();


					
								multiplicative_name();

								decryption_name();	
		
								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Decryption();


						

						Decryption();

					elif cyber=='3':
						clear();


						

						NAME();


			
						multiplicative_name();

						brute_name();
						def Brute():
							try:
								str=input("Enter the Text you want to Decrypt in Capital Alphabets Only : \n\n① Back\n\n② Exit"+"\033[A"*4+"\033[C"*57);



						

								clear();


						

								NAME();

								multiplicative_name();

								brute_name();

								def text():
									print("𝓔𝓷𝓬𝓻𝔂𝓹𝓽𝓮𝓭 𝓣𝓮𝔁𝓽 : "+'"'+str+'"\n'); 
								text();

								if str=="1":

									clear();


						

									NAME();

									multiplicative_name();
									Cyber();


								elif str=="2":

									exit();

								elif str=="":

									print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");

									Brute();

								char=False;
								ls=["[","@",";","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
										break;										
									elif c==chr(92):
										char=True;
										break;
									else:
										for i in ls:
											if i==c:

												char=True;
												break;
							
								if char==True:
									print("You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n");
									Brute();
									
								else:
									clear();
		
									NAME();

									multiplicative_name();

									brute_name();
			
									text();

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
														
											print("𝓚𝓮𝔂 : "+'"'+"{}".format(key)+'" '+"𝓟𝓵𝓪𝓲𝓷 𝓣𝓮𝔁𝓽 : "+'"'+decrypted_word+'"\n');
											decrypt_val=[];
											start=0;
									def User():

										try:
											user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
														
											if user=="1":
												clear();
												NAME();
												Cryptestein();
													
											elif user=="2":
												exit();
														
											elif user=="":
												print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
												clear();
												NAME();
												User();
						
											else:
												print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
												clear();
												NAME();
												User();
																											
										except KeyboardInterrupt:

											clear();


														

											NAME();


											
											print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
											User();

										except EOFError:

											clear();


														

											NAME();


											
											print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
											User();
									User();



							except KeyboardInterrupt:

								clear();


								

								NAME();


					
								multiplicative_name();

								decryption_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Brute();

							except EOFError:

								clear();


								

								NAME();


					
								multiplicative_name();

								decryption_name();	
		
								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Brute();


						Brute();
					elif cyber=="4":

						clear();


						
					
						NAME();

						Cryptestein();

					elif cyber=="5":
						exit();


					elif cyber=="":

			

						clear();


			
				
						NAME();
				

						multiplicative_name()	
			
				
						print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");


			

						Cyber();


					else:

						

						clear();


						
					
						NAME();
					
						multiplicative_name()	
	
						
						
						print("You Entered",'"'+cyber+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");


						
						Cyber();

				except KeyboardInterrupt:

					

					clear();


					
				
					NAME();


					multiplicative_name()	
					

					print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");
					Cyber();

				except EOFError:

					

					clear();


					
							
					NAME();


					multiplicative_name()	
					

					print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");
					Cyber();

			
			Cyber();


		elif cryptestein=='3':


			

			clear();


			

			NAME();

			def autokey_name():
				print("𝐀𝐮𝐭𝐨𝐊𝐞𝐲 𝐂𝐢𝐩𝐡𝐞𝐫\n")
			autokey_name()	

			

			def Autokey():

				try:


						

					autokey=input("① Encryption\n\n② Decryption\n\n③ Brute Force\n\n④ Back\n\n⑤ Exit\n\nChoose an Option : ");



					if autokey=='1':
			
						

						clear();


						

						NAME();

						autokey_name();

						encryption_name();


							

						def Encryption():	


							try:


							

								str=input("Enter the Text you want to Encrypt in Small Alphabets Only : \n\n① Back\n\n② Exit"+"\033[A"*4+"\033[C"*55);



						

								clear();


						

								NAME();

								autokey_name();

								encryption_name();

								def text():
									print("𝓟𝓵𝓪𝓲𝓷 𝓣𝓮𝔁𝓽 : "+'"'+str+'"\n'); 
								text();

								if str=="1":

									clear();


						

									NAME();

									autokey_name();
									Autokey();


								elif str=="2":

									exit();

								elif str=="":

									print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");

									Encryption();


							

								char=False;					
								ls=["[","@",";","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]
								for c in str:

									if c.isdigit() or c.isupper():

										char=True;
										break;
									elif c==chr(92):
										char=True;
										break;
									else:
										for i in ls:
											if i==c:

												char=True;
												break;


							

								if char==True:

									print("You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n");


							

									Encryption();

									
							

								else:
									def K(): 
										
										try:
											key=input("Enter the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters : \n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*91);


						

											clear();


						

											NAME();


											autokey_name();

											encryption_name();
			
											text();
											
											def key_name():
												print("𝓚𝓮𝔂 : "+'"'+key+'"\n');
											key_name();

											if key=="A":
												
												clear();


										

												NAME();

												autokey_name();
	
												encryption_name();

												Encryption();

											elif key=="B":
												exit();	

											elif key=="":

												print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");

												K();

							

											k=True;

											if key.isdigit()!=True:
												k=False

											elif int(key)>25:
												k=False

											elif int(key)<0:
												k=False


							
											if k==False:
												print("You did not Follow the Instructions and Entered",'"'+key+'",',"which contains unacceptable characters\n");


							

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


													
												print("𝓔𝓷𝓬𝓻𝔂𝓹𝓽𝓮𝓭 𝓣𝓮𝔁𝓽 : "+'"'+encrypted_word+'"\n');

												def User():

													try:
														user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
														
														if user=="1":
															clear();
															NAME();
															Cryptestein();
													
														elif user=="2":
															exit();
														
														elif user=="":
															print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
															clear();
															NAME();
															User();
						
														else:
															print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
															clear();
															NAME();
															User();
																												
													except KeyboardInterrupt:

														clear();


														

														NAME();


											
														print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
														User();

													except EOFError:

														clear();


														

														NAME();


											
														print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
														User();
												User();

										except KeyboardInterrupt:

											clear();


											

											NAME();


								
											autokey_name();

											encryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();

										except EOFError:

											clear();


											

											NAME();


								
											autokey_name();

											encryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();
										
									K();	


						
							except KeyboardInterrupt:

								clear();


								

								NAME();


					
								autokey_name();

								encryption_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");
								Encryption();

							except EOFError:

								clear();


								

								NAME();


					
								autokey_name();

								encryption_name();	
		
								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");
								Encryption();


						

						Encryption();

					elif autokey=='2':
						
						

						clear();


						

						NAME();


			
						autokey_name();

						decryption_name();


						

						def Decryption():	


							try:


						

								str=input("Enter the Text you want to Decrypt in Capital Alphabets Only : \n\n① Back\n\n② Exit"+"\033[A"*4+"\033[C"*57);



						

								clear();


						

								NAME();

								autokey_name();

								decryption_name();

								def text():
									print("𝓔𝓷𝓬𝓻𝔂𝓹𝓽𝓮𝓭 𝓣𝓮𝔁𝓽 : "+'"'+str+'"\n'); 
								text();

								if str=="1":

									clear();


						

									NAME();

									autokey_name();
									Autokey();


								elif str=="2":

									exit();

								elif str=="":

									print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");

									Decryption();


						

								char=False;			
								ls=["[","@",";","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
										break;									
									elif c==chr(92):
											char=True;
											break;
									else:
										for i in ls:
											if i==c:

												char=True;
												break;


								if char==True:

									print("You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n");


						

									Decryption();

								
						

								else:
									def K(): 
										
										try:
											key=input("Enter the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters : \n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*91);


						

											clear();


						

											NAME();


											autokey_name();

											decryption_name();
			
											text();
											
											def key_name():
												print("𝓚𝓮𝔂 : "+'"'+key+'"\n');
											key_name();

											if key=="A":
												
												clear();


										

												NAME();

												autokey_name();
	
												decryption_name();

												Decryption();

											elif key=="B":
												exit();	

											elif key=="":

												print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");

												K();


						

											k=True;

											if key.isdigit()!=True:
												k=False

											elif int(key)>25:
												k=False

											elif int(key)<0:
												k=False


						
											if k==False:
												print("You did not Follow the Instructions and Entered",'"'+key+'",',"which contains unacceptable characters\n");


						

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
												
												print("𝓟𝓵𝓪𝓲𝓷 𝓣𝓮𝔁𝓽 : "+'"'+decrypted_word+'"\n');

												def User():

													try:
														user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
														
														if user=="1":
															clear();
															NAME();
															Cryptestein();
													
														elif user=="2":
															exit();
														
														elif user=="":
															print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
															clear();
															NAME();
															User();
						
														else:
															print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
															clear();
															NAME();
															User();
																												
													except KeyboardInterrupt:

														clear();


														

														NAME();


											
														print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
														User();

													except EOFError:

														clear();


														

														NAME();


											
														print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
														User();
												User();


										except KeyboardInterrupt:

											clear();


											

											NAME();


								
											autokey_name();

											decryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();

										except EOFError:

											clear();


											

											NAME();


								
											autokey_name();

											decryption_name();	
					
											text();

											print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n");
											K();
										
									K();	


						
							except KeyboardInterrupt:

								clear();


								

								NAME();


					
								autokey_name();

								decryption_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Decryption();

							except EOFError:

								clear();


								

								NAME();


					
								autokey_name();

								decryption_name();	
		
								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Decryption();


						

						Decryption();
					

					elif autokey=='3':
						
						

						clear();


						

						NAME();


			
						autokey_name();

						brute_name();
						

						def Brute():
							
							
							try:


								str=input("Enter the Text you want to Decrypt in Capital Alphabets Only : \n\n① Back\n\n② Exit"+"\033[A"*4+"\033[C"*57);



						

								clear();


						

								NAME();

								autokey_name();

								brute_name();

								def text():
									print("𝓔𝓷𝓬𝓻𝔂𝓹𝓽𝓮𝓭 𝓣𝓮𝔁𝓽 : "+'"'+str+'"\n'); 
								text();

								if str=="1":

									clear();


						

									NAME();

									autokey_name();
									Autokey();


								elif str=="2":

									exit();

								elif str=="":

									print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");

									Brute();
									

								char=False;			
								
								ls=["[","@",";","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]

								for c in str:

									if c.isdigit() or c.islower():

										char=True;
										break;										
									elif c==chr(92):
										char=True;
										break;
									else:
										for i in ls:
											if i==c:

												char=True;
												break;


								if char==True:

									print("You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n");

									Brute();

								else:
									clear();
		
									NAME();

									autokey_name();

									brute_name();
			
									text();


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


										print("𝓚𝓮𝔂 : "+'"'+"{}".format(ky)+'" '+"𝓟𝓵𝓪𝓲𝓷 𝓣𝓮𝔁𝓽 : "+'"'+decrypted_word+'"\n');
										decrypt_val=[];
										start=0;
									def User():

										try:
											user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
														
											if user=="1":
												clear();
												NAME();
												Cryptestein();
													
											elif user=="2":
												exit();
														
											elif user=="":
												print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
												clear();
												NAME();
												User();
						
											else:
												print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
												clear();
												NAME();
												User();
																											
										except KeyboardInterrupt:

											clear();


														

											NAME();


											
											print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
											User();

										except EOFError:

											clear();


														

											NAME();


											
											print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
											User();
									User();

							except KeyboardInterrupt:

								clear();


								

								NAME();


					
								autokey_name();

								decryption_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Brute();

							except EOFError:

								clear();


								

								NAME();


					
								autokey_name();

								decryption_name();	
		
								print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n");
								Brute();


						Brute();

					elif autokey=="4":

						clear();


						
					
						NAME();

						Cryptestein();

					elif autokey=="5":
						exit();


					elif autokey=="":

			

						clear();


			
				
						NAME();
				

						autokey_name()	
			
				
						print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");


			

						Autokey();


					else:

						

						clear();


						
					
						NAME();
					
						autokey_name()	
	
						
						
						print("You Entered",'"'+autokey+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");


						
						Autokey();

				except KeyboardInterrupt:

					

					clear();


					
				
					NAME();


					autokey_name()	
					

					print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");
					Autokey();

				except EOFError:

					

					clear();


					
							
					NAME();


					autokey_name()	
					

					print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");
					Autokey();

			
			Autokey();

		elif cryptestein=='4':


			

			clear();


			

			NAME();

			def rsa_name():
				print("𝐑𝐒𝐀 𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦\n")
			rsa_name()	
			

			def RSA():

				try:


					
					Rsa=input("① Private Key\n\n② Encryption / Decryption\n\n③ Back\n\n④ Exit\n\nChoose an Option : ");
					
					if Rsa=='1':

						clear();


						

						NAME();

						rsa_name();

						key_name();
					
						def Prime1():

							try:
							
								prime1=input("Enter First Prime Number : \n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*19);
								clear();


						

								NAME();

								rsa_name();

								key_name();

								def prime1_name():
									print("𝓕𝓲𝓻𝓼𝓽 𝓟𝓻𝓲𝓶𝓮: "+'"'+prime1+'"\n'); 
								prime1_name();

								if prime1=="A":

									clear();


						

									NAME();

									rsa_name();
									RSA();


								elif prime1=="B":

									exit();

								elif prime1=="":

									print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");

									Prime1();

								char=False;
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~"," ","+",";",":",".","=","-","`",",","]"]								

								for c in prime1:

									if c.isalpha():

										char=True;
										break;
									
									elif c==chr(92):
										char=True;
										break;			
			
									else:
										for i in ls:
											if i==c:

												char=True;
												break;
								if char==True:
									print('"'+prime1+'"',"is not a Prime Number\n");	

									Prime1();
								else:
									if int(prime1)>1:
										
										for i in range(2,int(prime1)):

											if int(prime1)%i==0:
												print('"'+prime1+'"',"is not a Prime Number\n");	
												Prime1();
												break;

										else:

											def Prime2():

												try:

													prime2=input("Enter Second Prime Number which is different from first prime number you entered : \n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*75);

													clear();


											

													NAME();

													rsa_name();

													key_name();

													prime1_name();

													def prime2_name():
														print("𝓢𝓮𝓬𝓸𝓷𝓭 𝓟𝓻𝓲𝓶𝓮 : "+'"'+prime2+'"\n'); 
													prime2_name();

													if prime2=="A":

														clear();


											

														NAME();

														rsa_name();

														key_name();

														Prime1();


													elif prime2=="B":

														exit();

													elif prime2=="":

														print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number different from first Prime Number\n");

														Prime2();


													char=False;
													ls=["[","@","_","!","#","$","%","^","&","*","(",")"," ","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

													for c in prime2:

														if c.isalpha():

															char=True;
															break;										

														elif c==chr(92):
															char=True;
															break;

														else:
															for i in ls:
																if i==c:

																	char=True;
																	break;
									
													if char==True:
														print('"'+prime2+'"',"is not a Prime Number\n");	
														Prime2();

													if int(prime2)!=int(prime1):

														if int(prime2)>1:
															for i in range(2,int(prime2)):

																if int(prime2)%i==0:
																	print('"'+prime2+'"',"is not a Prime Number\n");	
																	Prime2();

															else:

																n=int(prime1)*int(prime2);

																phie_n=(int(prime1)-1)*(int(prime2)-1);

																def E():

																	try:

																		e=input("Enter the Value of Public Key which is Greater Than 1 and Less Than {} : ".format(phie_n)+"\n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*(64+len(str(phie_n))-1));

																		clear();


																

																		NAME();

																		rsa_name();

																		key_name();

																		prime1_name();

																		prime2_name();

																		def public_key_name():
																			print("𝓟𝓾𝓫𝓵𝓲𝓬 𝓚𝓮𝔂 : "+'"'+e+'"\n'); 
																		public_key_name();

																		if e=="A":

																			clear();


																

																			NAME();

																			rsa_name();

																			key_name();

																			prime1_name();

																			Prime2();


																		elif e=="B":

																			exit();

																		elif e=="":

																			print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Number for Public Key which is Greater Than 1 and Less Than {}\n".format(phie_n));

																			E();

																		char=False;
																		ls=["[","@","_","!","#","$","%","^","&","*","(",")"," ","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

																		for c in e:

																			if c.isalpha():

																				char=True;
																				break;

																			elif c==chr(92):
																				char=True;
																				break;								
																			else:
																				for i in ls:
																					if i==c:

																						char=True;
																						break;

																		if char==True:
																			print('"'+e+'"',"is not a Valid Public Key\n");	
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
																					clear();


																		

																					NAME();

																					rsa_name();

																					key_name();

															
																					print("The GCD of "+e+" and {}".format(phie_n)+" is not equal to 1\n");
															
																					Prime1();

																				else:
															
																					i=1;
																					while True:
																						if (phie_n*i+1)%int(e)==0:
																							d=(phie_n*i+1)//int(e);
																							break;
																						else:
																							i=i+1;
																					print("𝓟𝓻𝓲𝓿𝓪𝓽𝓮 𝓚𝓮𝔂 : "+'"{}'.format(d)+'"\n');
								
																					def User():

																						try:
																							user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
																										
																							if user=="1":
																								clear();
																								NAME();
																								Cryptestein();
																									
																							elif user=="2":
																								exit();
																										
																							elif user=="":
																								print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
																								clear();
																								NAME();
																								User();
																		
																							else:
																								print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
																								clear();
																								NAME();
																								User();
																																							
																						except KeyboardInterrupt:

																							clear();


																										

																							NAME();


																							
																							print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
																							User();

																						except EOFError:

																							clear();


																										

																							NAME();


																							
																							print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
																							User();
																					User();

																			else:
																				print("You did not entered the value between 1 and",phie_n,"\n");
																				E();
																	except KeyboardInterrupt:

																		clear();


																		

																		NAME();


															
																		rsa_name();

																		key_name();

																		prime1_name();

																		prime2_name();

																		print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
																		E();

																	except EOFError:

																		clear();


																		

																		NAME();


															
																		rsa_name();

																		key_name();

																		prime1_name();

																		prime2_name();

																		print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
																		E();


																E();

														else:
															print('"'+prime2+'"',"is not a Prime Number\n");	

															Prime2();
													else:
														print('"'+prime2+'"',"is equal to the First Prime Number you Entered\n");	
														Prime2();

												except KeyboardInterrupt:

													clear();


													

													NAME();


										
													rsa_name();

													key_name();

													prime1_name();
													print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
													Prime2();

												except EOFError:

													clear();


													

													NAME();


										
													rsa_name();

													key_name();

													prime1_name();
													print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
													Prime2();


											Prime2();
									else:
										print('"'+prime1+'"',"is not a Prime Number\n");	
										Prime1();
							except KeyboardInterrupt:

								clear();


								

								NAME();


					
								rsa_name();

								key_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
								Prime1();

							except EOFError:

								clear();


								

								NAME();


					
								rsa_name();

								key_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
								Prime1();


						Prime1();

					elif Rsa=='2':

						clear();


						

						NAME();

						rsa_name();

						encryption_decryption_name();
					
						def Prime1():

							try:
							
								prime1=input("Enter First Prime Number : \n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*19);
								clear();


						

								NAME();

								rsa_name();

								encryption_decryption_name();

								def prime1_name():
									print("𝓕𝓲𝓻𝓼𝓽 𝓟𝓻𝓲𝓶𝓮: "+'"'+prime1+'"\n'); 
								prime1_name();

								if prime1=="A":

									clear();


						

									NAME();

									rsa_name();
									RSA();


								elif prime1=="B":

									exit();

								elif prime1=="":

									print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");

									Prime1();

								char=False;
								ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~"," ","+",";",":",".","=","-","`",",","]"]								

								for c in prime1:

									if c.isalpha():

										char=True;
										break;
									
									elif c==chr(92):
										char=True;
										break;			
			
									else:
										for i in ls:
											if i==c:

												char=True;
												break;
								if char==True:
									print('"'+prime1+'"',"is not a Prime Number\n");	

									Prime1();
								else:
									if int(prime1)>1:
										
										for i in range(2,int(prime1)):

											if int(prime1)%i==0:
												print('"'+prime1+'"',"is not a Prime Number\n");	
												Prime1();
												break;

										else:

											def Prime2():

												try:

													prime2=input("Enter Second Prime Number which is different from first prime number you entered : \n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*75);

													clear();


											

													NAME();

													rsa_name();

													encryption_decryption_name();

													prime1_name();

													def prime2_name():
														print("𝓢𝓮𝓬𝓸𝓷𝓭 𝓟𝓻𝓲𝓶𝓮 : "+'"'+prime2+'"\n'); 
													prime2_name();

													if prime2=="A":

														clear();


											

														NAME();

														rsa_name();

														encryption_decryption_name();

														Prime1();


													elif prime2=="B":

														exit();

													elif prime2=="":

														print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number different from first Prime Number\n");

														Prime2();


													char=False;
													ls=["[","@","_","!","#","$","%","^","&","*","(",")"," ","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

													for c in prime2:

														if c.isalpha():

															char=True;
															break;										

														elif c==chr(92):
															char=True;
															break;

														else:
															for i in ls:
																if i==c:

																	char=True;
																	break;
									
													if char==True:
														print('"'+prime2+'"',"is not a Prime Number\n");	
														Prime2();

													if int(prime2)!=int(prime1):

														if int(prime2)>1:
															for i in range(2,int(prime2)):

																if int(prime2)%i==0:
																	print('"'+prime2+'"',"is not a Prime Number\n");	
																	Prime2();

															else:

																n=int(prime1)*int(prime2);

																phie_n=(int(prime1)-1)*(int(prime2)-1);

																def E():

																	try:

																		e=input("Enter the Value of Public Key which is Greater Than 1 and Less Than {} : ".format(phie_n)+"\n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*(64+len(str(phie_n))-1));

																		clear();


																

																		NAME();

																		rsa_name();

																		encryption_decryption_name();

																		prime1_name();

																		prime2_name();

																		def public_key_name():
																			print("𝓟𝓾𝓫𝓵𝓲𝓬 𝓚𝓮𝔂 : "+'"'+e+'"\n'); 
																		public_key_name();

																		if e=="A":

																			clear();


																

																			NAME();

																			rsa_name();

																			encryption_decryption_name();

																			prime1_name();

																			Prime2();


																		elif e=="B":

																			exit();

																		elif e=="":

																			print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Number for Public Key which is Greater Than 1 and Less Than {}\n".format(phie_n));

																			E();

																		char=False;
																		ls=["[","@","_","!","#","$","%","^","&","*","(",")"," ","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

																		for c in e:

																			if c.isalpha():

																				char=True;
																				break;

																			elif c==chr(92):
																				char=True;
																				break;								
																			else:
																				for i in ls:
																					if i==c:

																						char=True;
																						break;

																		if char==True:
																			print('"'+e+'"',"is not a Valid Public Key\n");	
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
																					clear();


																		

																					NAME();

																					rsa_name();

																					encryption_decryption_name();

															
																					print("The GCD of "+e+" and {}".format(phie_n)+" is not equal to 1\n");
															
																					Prime1();

																				else:
															
																					i=1;
																					while True:
																						if (phie_n*i+1)%int(e)==0:
																							d=(phie_n*i+1)//int(e);
																							break;
																						else:
																							i=i+1;

																					def private_key_name():																								
																						print("𝓟𝓻𝓲𝓿𝓪𝓽𝓮 𝓚𝓮𝔂 : "+'"{}'.format(d)+'"\n');
																					private_key_name();


																					def Choice():
												
																						try:
					
																							choice=input("① Encryption\n\n② Decryption\n\n③ Back\n\n④ Exit\n\nChoose an Option : ");
																							

																							if choice=='1':
			
						

																								clear();


																						

																								NAME();

																								rsa_name();

																								encryption_decryption_name();

																								prime1_name();

																								prime2_name();

																								public_key_name();
				
																								private_key_name();

																								encryption_name();
						

																								def Encryption():	


																									try:


						

																										str=input("Enter the Text you want to Encrypt in Small Alphabets Only : \n\n① Back\n\n② Exit"+"\033[A"*4+"\033[C"*55);



						

																										clear();


																								

																										NAME();

																										rsa_name();

																										encryption_decryption_name();

																										prime1_name();

																										prime2_name();

																										public_key_name();
						
																										private_key_name();

																										encryption_name();

																										def text():
																											print("𝓟𝓵𝓪𝓲𝓷 𝓣𝓮𝔁𝓽 : "+'"'+str+'"\n'); 
																										text();


																										if str=="1":

																											clear();


																									

																											NAME();

																											rsa_name();

																											encryption_decryption_name();

																											prime1_name();

																											prime2_name();

																											public_key_name();

																											private_key_name();

																											Choice();

																										elif str=="2":

																											exit();

																										elif str=="":

																											print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");

																											Encryption();
						

																										char=False;					
																										ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]
																										for c in str:

																											if c.isdigit() or c.isupper():

																												char=True;
																												break;

																											elif c==chr(92):
																												char=True;
																												break;
						
																											else:
																												for i in ls:
																													if i==c:

																														char=True;
																														break;

						

																										if char==True:

																											print("You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n");


						

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

																											print("𝓔𝓷𝓬𝓻𝔂𝓹𝓽𝓮𝓭 𝓣𝓮𝔁𝓽 : "+'"'+encrypted_word+'"\n');

																											def User():

																												try:
																													user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
																													
																													if user=="1":
																														clear();
																														NAME();
																														Cryptestein();
																												
																													elif user=="2":
																														exit();
																													
																													elif user=="":
																														print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
																														clear();
																														NAME();
																														User();
																					
																													else:
																														print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
																														clear();
																														NAME();
																														User();
																																											
																												except KeyboardInterrupt:

																													clear();


																													

																													NAME();


																										
																													print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
																													User();

																												except EOFError:

																													clear();


																													

																													NAME();


																										
																													print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
																													User();
																											User();

																									except KeyboardInterrupt:

																										clear();


																								

																										NAME();

																										rsa_name();

																										encryption_decryption_name();

																										prime1_name();

																										prime2_name();

																										public_key_name();

																										private_key_name();

																										encryption_name();

																										print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");
																										Encryption();

																									except EOFError:

																										clear();


																								

																										NAME();

																										rsa_name();

																										encryption_decryption_name();

																										prime1_name();

																										prime2_name();

																										public_key_name();
																				
																										private_key_name();

																										encryption_name();

																										print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");
			
																										Encryption();


																								

																								Encryption();


																							elif choice=='2':
			
						

																								clear();


																						

																								NAME();

																								rsa_name();

																								encryption_decryption_name();

																								prime1_name();

																								prime2_name();

																								public_key_name();
				
																								private_key_name();

																								decryption_name();

						

																								def Decryption():	


																									try:

																										str=input("Enter the Text you want to Decrypt in Numbers or Spaces, Separated with Commas only : \n\n(𝓐) Back\n\n(𝓑) Exit"+"\033[A"*4+"\033[C"*78);
																										clear();


																								

																										NAME();

																										rsa_name();

																										encryption_decryption_name();

																										prime1_name();

																										prime2_name();

																										public_key_name();
						
																										private_key_name();

																										decryption_name();

																										def text():
																											print("𝓔𝓷𝓬𝓻𝔂𝓹𝓽𝓮𝓭 𝓣𝓮𝔁𝓽 : "+'"'+str+'"\n'); 
																										text();


																										if str=="A":

																											clear();


																									

																											NAME();

																											rsa_name();

																											encryption_decryption_name();

																											prime1_name();

																											prime2_name();

																											public_key_name();

																											private_key_name();

																											Choice();

																										elif str=="B":

																											exit();

																										elif str=="":

																											print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered Text you want to Decrypt in Numbers or Spaces, Separated with Commas only\n");

																											Decryption();
						

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

																											print("You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n");


						

																											Decryption();

																										else:
					
																											characters=str.split(",");
																																	
																											index=[];
																											for i in characters:
																												if i==" "*len(i):
																													for i in range(len(i)):
																														index.append(32);
																												else:
																													index.append(i);

																											for i in index:
																												if i=="":
																													print("At somewhere in the encrypted text, you entered consicutive commas and there was no number or space between them\n");
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
																											print("𝓟𝓵𝓪𝓲𝓷 𝓣𝓮𝔁𝓽 : "+'"'+decrypted_word+'"\n');

																											def User():

																												try:
																													user=input("① Continue\n\n② Exit\n\nChoose an Option : ");
																													
																													if user=="1":
																														clear();
																														NAME();
																														Cryptestein();
																												
																													elif user=="2":
																														exit();
																													
																													elif user=="":
																														print("You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'1'"' or '"'2'"'");
																														clear();
																														NAME();
																														User();
																					
																													else:
																														print("You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n");			
																														clear();
																														NAME();
																														User();
																																											
																												except KeyboardInterrupt:

																													clear();


																													

																													NAME();


																										
																													print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
																													User();

																												except EOFError:

																													clear();


																													

																													NAME();


																										
																													print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n");
																													User();
																											User();

																									except KeyboardInterrupt:

																										clear();


																								

																										NAME();

																										rsa_name();

																										encryption_decryption_name();

																										prime1_name();

																										prime2_name();

																										public_key_name();

																										private_key_name();

																										decryption_name();

																										print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");
																										Decryption();

																									except EOFError:

																										clear();


																								

																										NAME();

																										rsa_name();

																										encryption_decryption_name();

																										prime1_name();

																										prime2_name();

																										public_key_name();
																				
																										private_key_name();

																										decryption_name();

																										print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n");
			
																										Decryption();


																								

																								Decryption();
																					
																							elif choice=="3":

																								clear();


																						

																								NAME();

																								rsa_name();

																								encryption_decryption_name();

																								prime1_name();

																								prime2_name();

																								E();
																							elif choice=="4":
																								exit();


																							elif choice=="":

																					

																								clear();


																						

																								NAME();

																								rsa_name();

																								encryption_decryption_name();

																								prime1_name();

																								prime2_name();

																								public_key_name();
				
																								private_key_name();																																									
																						
																								print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"'\n");


																					

																								Choice();


																							else:

																								

																								clear();


																						

																								NAME();

																								rsa_name();

																								encryption_decryption_name();

																								prime1_name();

																								prime2_name();

																								public_key_name();
																			
																								private_key_name();
																								
																								print("You Entered",'"'+choice+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"'\n");


																								Choice();
																						
																						except KeyboardInterrupt:

																							

																							clear();


																						

																							NAME();

																							rsa_name();

																							encryption_decryption_name();

																							prime1_name();

																							prime2_name();

																							public_key_name();
																							
																							private_key_name();


																							print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"'\n");
																							Choice();

																						except EOFError:

																							

																							clear();


																						

																							NAME();

																							rsa_name();

																							encryption_decryption_name();

																							prime1_name();

																							prime2_name();

																							public_key_name();
																							
																							private_key_name();


																							print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"'\n");
																							Choice();
																							
																					
																					Choice();
																			else:
																				print("You did not entered the value between 1 and",phie_n,"\n");
																				E();
																	except KeyboardInterrupt:

																		clear();


																		

																		NAME();


															
																		rsa_name();

																		encryption_decryption_name();

																		prime1_name();

																		prime2_name();

																		print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
																		E();

																	except EOFError:

																		clear();


																		

																		NAME();


															
																		rsa_name();

																		encryption_decryption_name();

																		prime1_name();

																		prime2_name();

																		print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
																		E();


																E();

														else:
															print('"'+prime2+'"',"is not a Prime Number\n");	

															Prime2();
													else:
														print('"'+prime2+'"',"is equal to the First Prime Number you Entered\n");	
														Prime2();

												except KeyboardInterrupt:

													clear();


													

													NAME();


										
													rsa_name();

													encryption_decryption_name();

													prime1_name();
													print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
													Prime2();

												except EOFError:

													clear();


													

													NAME();


										
													rsa_name();

													encryption_decryption_name();

													prime1_name();
													print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
													Prime2();


											Prime2();
									else:
										print('"'+prime1+'"',"is not a Prime Number\n");	
										Prime1();
							except KeyboardInterrupt:

								clear();


								

								NAME();


					
								rsa_name();

								encryption_decryption_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
								Prime1();

							except EOFError:

								clear();


								

								NAME();


					
								rsa_name();

								encryption_decryption_name();

								print("You Interrupted the Working of the Program, you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered a Prime Number\n");
								Prime1();


						Prime1();

					elif Rsa=="3":

						clear();


						
					
						NAME();

						Cryptestein();

					elif Rsa=="4":
						exit();


					elif Rsa=="":

			

						clear();


			
				
						NAME();
				

						rsa_name()	
			
				
						print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"'\n");


			

						RSA();


					else:

						

						clear();


						
					
						NAME();
					
						rsa_name()	
	
						
						
						print("You Entered",'"'+Rsa+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"'\n");


						
						RSA();

				except KeyboardInterrupt:

					

					clear();


					
				
					NAME();


					rsa_name()	
					

					print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"'\n");
					RSA();

				except EOFError:

					

					clear();


					
							
					NAME();


					rsa_name()	
					

					print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");
					RSA();

			
			RSA();

		elif cryptestein=="5":
			exit();

		elif cryptestein=="":

			

			clear();


			
				
			NAME();
				

			
				
			print("You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");


			

			Cryptestein();
			
		else:

			

			clear();


			
				
			NAME();
				

			
				
			print("You Entered",'"'+cryptestein+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");


			

			Cryptestein();


	

	except KeyboardInterrupt:

		

		clear();


		
				
		NAME();


		

		print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");
		Cryptestein();

	except EOFError:

		

		clear();


		
				
		NAME();


		

		print("You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n");
		Cryptestein();



Cryptestein();
