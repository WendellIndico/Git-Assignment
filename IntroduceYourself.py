#include <iostream>
#include <string>

using namespace std;

void printMainBorder() {
    cout << "=====================================================" << endl;
}

void printSectionDivider() {
    cout << "-----------------------------------------------------" << endl;
}

void showStudentProfile(string pet, string name, string bday, string addr, string song, string motive, string supp) {
    
    printMainBorder();
    cout << "                  GET TO KNOW ME!                    " << endl;
    printMainBorder();
    
    if (pet == "Dog" || pet == "dog") {
        cout << "  🐶 🐶 🐶         ABOUT ME PROFILE         🐶 🐶 🐶  " << endl;
    } else {
        cout << "  🐱 🐱 🐱         ABOUT ME PROFILE         🐱 🐱 🐱  " << endl;
    }
    
    printSectionDivider();
    
    cout << "  👤 Name       : " << name << endl;
    cout << "  🎂 Birthday   : " << bday << endl;
    cout << "  📍 Address    : " << addr << endl;
    cout << "  🎵 Fav Song   : " << song << endl;
    cout << "  ❤️ Motivation : " << motive << endl;
    cout << "  🤝 Support    : " << supp << endl;
    
    printSectionDivider(); 
    
    cout << "          THANKYOU FOR GETTING TO KNOW ME!           " << endl;
    printMainBorder();
}

int main() {
    string petChoice = "Dog"; 
    string name      = "WENDELL L. INDICO / Wendell";
    string birthday  = "11/01/2004";
    string address   = "TABUC SUBA, JARO, ILOILO CITY";
    string favSong   = "Sagip / Jan Roberts"; 
    string motive    = "MY FAMILY";
    string support   = "Good Teachers!";

    showStudentProfile(petChoice, name, birthday, address, favSong, motive, support);

    return 0;
}# Profile Script 
