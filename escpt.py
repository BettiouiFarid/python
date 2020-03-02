while True:
    try:
        num = int(input("veuillez entrer un numero:\n"))
        print(18 / num)
        break
    except ValueError:  # erreur
        print("verifier la valeur")
    except ZeroDivisionError:
        print("ops 0 n'est pas disponible")
    finally:
        print("excute this no mattre what")
