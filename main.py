import bcrypt

from database import *

from encryption import *

from password_generator import *



create_tables()



while True:


    print("\nSECURE PASSWORD MANAGER")


    print("1.Register")

    print("2.Login")

    print("3.Exit")


    choice=input("Enter choice:")



    if choice=="1":


        username=input("Username:")

        password=input("Password:")



        hashed=bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
        )


        add_user(
        username,
        hashed
        )


        print("Account Created")




    elif choice=="2":


        username=input("Username:")

        password=input("Password:")



        result=check_user(username)



        if result and bcrypt.checkpw(
        password.encode(),
        result[0]):


            print("Login Successful")



            while True:


                print("\n1.Add Password")

                print("2.View Password")

                print("3.Generate Password")

                print("4.Logout")


                op=input("Choice:")



                if op=="1":


                    site=input("Website:")

                    user=input("Email:")

                    pwd=input("Password:")


                    encrypted=encrypt(pwd)


                    save_password(
                    site,
                    user,
                    encrypted
                    )


                    print("Saved")



                elif op=="2":


                    data=get_passwords()


                    for x in data:

                        print(
                        x[1],
                        x[2],
                        decrypt(x[3])
                        )

                elif op=="3":

                    print(
                    generate()
                    )

                elif op=="4":

                    break

        else:

            print("Wrong Login")
    else:
        break