class Message:
    message = "Mon Message";
    decalage = 0;

    def __init__(this, message):
        this.message = message

    def afficher(this):
        print this.message;

    def afficher_decalage(this):
        print this.decalage;

    def set_decalage(this, decalage):
        this.decalage = int(int(decalage) % 26);

    def scan_decalage(this):
        input = raw_input("Entrez le decalage:  ");
        print "Vous avez choisi  ", input;
        this.set_decalage(input);

    def set_message(this, message):
        this.message = message;

    def scan_message(this):
        input = raw_input("Entrez le message:  ");
        print "Vous avez choisi  ", input;
        this.set_message(input);

    def crypter(this):
        res = ""
        for c in this.message:
            if c == " ":
                res += " ";
            else:
                res += chr(((ord(c)- 65 + this.decalage) % 26) + 65);
        this.message = res;

    def decrypter(this):
        res = ""
        for c in this.message:
            if c == " ":
                res += " ";
            else:
                res += chr(((ord(c)- 65 - this.decalage) % 26) + 65);
        this.message = res;

class Analyse(Message):
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    plus_utilise = ['E','A','S','']
    count_max = -1

    def __init__(this, message):
        this.set_message(message);

    def afficher_count(this):
        print this.count;

    def compter_lettre(this):
        for c in this.message:
            if c != " ":
                this.count[(ord(c) - 65) % 26] += 1;

    def get_id_max(this):
        max = 0
        id  = -1
        for i in range(len(this.count)):
            if this.count[i] > max:
                max = this.count[i];
                id = i;
        this.count_max = id;

    def







message = Analyse("MON MESSAGE");
message.compter_lettre();
message.afficher_count();
message.get_max();


class Demo_automatique(Message):
    def __init__(this):
        this.set_message("MON MESSAGE");
        this.set_decalage(6);
        this.crypter();
        this.afficher();
        this.decrypter();
        this.afficher();

class Demo(Message):
    def __init__(this):
        this.scan_message();
        this.scan_decalage();
        this.crypter();
        this.afficher();
        this.decrypter();
        this.afficher();
