# primo match

ordine = input("inserisci il tuo ordine: ")

match ordine:
    case "pizza": ## Se l'ordine è "pizza"
        print("Hai ordinato una pizza")
    case "pasta": ## Se l'ordine è "pasta"
        print("Hai ordinato una pasta")
    case "insalata": ## Se l'ordine è "insalata"
        print("Hai ordinato un'insalata")
    case _: ## Se l'ordine non corrisponde a nessuno dei casi precedenti
        print("Ordine non riconosciuto")