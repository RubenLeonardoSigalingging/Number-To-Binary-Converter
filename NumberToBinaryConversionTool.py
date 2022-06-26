#!/usr/bin/env python3


from os import system
system("clear")
system("chmod 777 NumberToBinaryConversionTool.py")


def number_to_binary_converter_tool(created_by="Ruben Leonardo Sigalingging."):
	from pyfiglet import figlet_format
	tema=figlet_format("Converter",font="slant")
	print(tema)
	print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Minggu, 26 Juni 2022, Pukul 7:29 PM.")
	print("[!] Fungsi: Untuk Mengkonversi Nomor Ke Kode Biner.\n")
	number=int(input("[!] Enter Number: "))
	binary=bin(number)[2:]
	print(f"[!] Binary Code Of {number} Is: {binary}")
number_to_binary_converter_tool()


# https://www.rapidtables.com/convert/number/binary-to-decimal.html