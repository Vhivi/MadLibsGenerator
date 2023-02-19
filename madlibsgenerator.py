#!/usr/bin/python
# -*- coding: utf-8 -*-

# Mad Libs Generator
# La conception du programme est telle qu'il demandera aux utilisateurs
# d'entrer une série d'entrées qui seront considérées comme un Mad Lib.
#
# L'entrée peut être n'importe quoi, un adjectif, un nom, un pronom, etc. Une
# fois toutes les entrées saisies, l'application prendra les données et les
# organisera sous la forme d'un modèle d'histoire. Puis affichera le résultat.

def main():
    print("Mad Libs Generator")
    print("")
    print("Merci d'entrer les mots suivants pour compléter l'histoire.")
    print("")

    name1 = input("Un nom : ")
    name2 = input("Un nom au pluriel : ")
    verb1 = input("Un verbe : ")
    verb2 = input("Un verbe : ")
    adj1 = input("Un adjectif féminin pluriel : ")
    adj2 = input("Un adjectif masculin singulier : ")
    adj3 = input("Un adjectif masculin singulier : ")

    print("")
    print("L'histoire de "+ name1 +", se déroule dans une galaxie qui est le")
    print("théâtre d'affrontements entre les "+ name2 +" et les")
    print("Seigneurs Sith, personnes "+ adj1 +" sensibles à la Force, un")
    print("champ "+ adj2 +" mystérieux leur procurant des pouvoirs")
    print(adj3 +". Les "+ name2 +" maîtrisent le Côté lumineux de la Force,")
    print("pouvoir bénéfique et défensif, pour "+ verb1 +" la paix dans la")
    print("galaxie. Les Sith utilisent le Côté obscur, pouvoir "+ adj3 +" et")
    print("destructeur, pour leurs usages personnels et pour "+ verb2 +" la")
    print("galaxie.")

main()
