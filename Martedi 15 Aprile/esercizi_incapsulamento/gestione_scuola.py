

class Persona:
    def __init__(self, nome, eta ):
        self.__nome = nome
        self.__eta = eta
    def get_nome(self):
        return self.__nome
    def get_eta(self):
        return self.__eta
    def set_nome(self, nome):
        self.__nome = nome
    def set_eta(self, eta):
        self.__eta = eta
    
    def presentazione(self):
        print(f"Nome: {self.__nome}, Eta: {self.__eta}")

class Studente(Persona):
      def __init__(self, nome, eta, voti):
          super().__init__(nome, eta)
          self.__voti = voti
      
      def get_voti(self):
          return self.__voti
      def set_voti(self, voti):
          self.__voti = voti
      
      def __media_voti(self):
          if not self.__voti:
              return 0
          return sum(self.__voti) / len(self.__voti)
      def presentazione(self):
          media = self.__media_voti()
          print(f"Ciao sono: {self.get_nome()}, ho: {self.get_eta()} anni e la mia media voti è di: {media:.2f}")

class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia
    def get_materia(self):
        return self.__materia
    def set_materia(self, materia):
        self.__materia = materia
    def presentazione(self):
          print(f"Salve sono: {self.get_nome()}, ho: {self.get_eta()} anni e sono il professore di: {self.__materia}")

class Scuola:
    def __init__(self, nome):
        self.__nome = nome
        self.__studenti = []
        self.__professori = []
        
    def aggiungi_studente(self, studente):
        if isinstance(studente, Studente):
            self.__studenti.append(studente)
    def aggiungi_professore(self, professore):
        if isinstance(professore, Professore):
            self.__professori.append(professore)
    def stampa_studenti(self):
        print(f"Elenco studenti nella scuola {self.__nome}:")
        for studente in self.__studenti:
            studente.presentazione()
    def stampa_professori(self):
        print(f"Elenco professori nella scuola {self.__nome}:")
        for professore in self.__professori:
            professore.presentazione()

def menu():
    scuola = Scuola("Scuola di Informatica")
    while True:
        print("1. Aggiungi studente")
        print("2. Aggiungi professore")
        print("3. Stampa studenti")
        print("4. Stampa professori")
        print("5. Esci")
        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                nome = input("Nome studente: ")
                eta = int(input("Età: "))
                voti_input = input("Inserisci i voti separati da virgola (es. 7,8,9): ")
                voti = [int(v) for v in voti_input.split(",") if v.strip().isdigit()]
                scuola.aggiungi_studente(Studente(nome, eta, voti))
                print("Studente aggiunto.")

            case "2":
                nome = input("Nome professore: ")
                eta = int(input("Età: "))
                materia = input("Materia insegnata: ")
                scuola.aggiungi_professore(Professore(nome, eta, materia))
                print("Professore aggiunto.")

            case "3":
                scuola.stampa_studenti()

            case "4":
                scuola.stampa_professori()

            case "5":
                print("Uscita dal programma.")
                break

menu()