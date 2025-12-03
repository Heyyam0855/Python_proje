#!/usr/bin/env python3
"""
Python Projesi - Temel Python Örneği
(Python Project - Basic Python Example)

Bu dosya Python ile ilgili temel özellikleri göstermektedir.
(This file demonstrates basic Python features.)
"""


def merhaba_dunya():
    """Merhaba Dünya fonksiyonu - Prints Hello World in Turkish"""
    print("Merhaba Dünya!")
    return "Merhaba Dünya!"


def toplama(a, b):
    """İki sayıyı toplar - Adds two numbers"""
    return a + b


def cikarma(a, b):
    """İki sayıyı çıkarır - Subtracts two numbers"""
    return a - b


def carpma(a, b):
    """İki sayıyı çarpar - Multiplies two numbers"""
    return a * b


def bolme(a, b):
    """İki sayıyı böler - Divides two numbers"""
    if b == 0:
        raise ValueError("Sıfıra bölme hatası! (Division by zero error!)")
    return a / b


def main():
    """Ana fonksiyon - Main function"""
    print("Python Projesi Hoş Geldiniz!")
    print("(Welcome to Python Project!)")
    print("-" * 40)
    
    # Temel hesaplama örnekleri
    # Basic calculation examples
    print("\nTemel Hesaplamalar (Basic Calculations):")
    print(f"5 + 3 = {toplama(5, 3)}")
    print(f"10 - 4 = {cikarma(10, 4)}")
    print(f"6 * 7 = {carpma(6, 7)}")
    print(f"20 / 4 = {bolme(20, 4)}")
    
    print("\n" + "-" * 40)
    merhaba_dunya()


if __name__ == "__main__":
    main()
