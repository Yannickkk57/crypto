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
    plus_utilise = ['E','A','S','I','N','T','R','L','U','O','D','C','P','M','V','G','F','B','Q','H','X','J','Y','Z','K','W'];


    def __init__(this, message):
        this.set_message(message);

    def afficher_count(this):
        print this.count;

    def compter_lettre(this):
        for c in this.message:
            if c != " ":
                this.count[(ord(c) - 65) % 26] += 1;

    def get_id_max_and_remove(this):
        this.afficher_count();
        max = 0;
        id  = -1;
        for i in range(len(this.count)):
            if this.count[i] > max:
                max = this.count[i];
                id = i;
                this.count[i] = -1;
                return id;
        return 0;

    def maj_to_min(this):
        res = "";
        for c in this.message:
            if c == " ":
                res += " ";
            else:
                res += chr(ord(c) + 32);
        this.set_message(res);

    def replace(this, c1, c2):
        res = "";
        for c in this.message:
            if c == c1:
                res += c2;
            else:
                res += c;
        this.set_message(res);

    def maj_to_min_char(this, c):
        return chr(ord(c) + 32);

    def decrypter_avec_frequence(this):
        this.compter_lettre();
        this.afficher_count();
        this.maj_to_min();
        for c in this.plus_utilise:
            this.replace(chr(this.get_id_max_and_remove() + 97), c);

    def test(this):
        this.maj_to_min();
        this.replace('j', 'i');




message = Analyse("UN JOUR JE SERAIS LE MEILLEUR DRESSEUR JE ME BATTRAIS SANS REPIT JE FERAIS TOUT POUR ETRE VAINQUEUR");
message.set_decalage(3);
message.afficher();
message.crypter();
message.afficher();
message.decrypter();
message.afficher();

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
