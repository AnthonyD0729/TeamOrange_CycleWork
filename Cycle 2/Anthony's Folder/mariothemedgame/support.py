from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for information in walk(path):
        print(information)
import_folder('../gra[hics/character/run')