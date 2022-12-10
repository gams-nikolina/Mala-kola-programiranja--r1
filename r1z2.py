#Napravi program koji će ti pomoći pri računanju koliko čokolada možeš kupiti s unesenom svotom novca. Također, izračunaj koliko eura će ti ostati nakon kupnje čokolada. Ostatak novca neka bude zaokružen na dvije decimale. (Koristi round)

a=float(input("Unesite koliko eura imate:"))
cijena_cokolade=1.23
broj_cokolada=a//1.23
ostatak_eura=a%1.23

print("Možeš kupiti" , broj_cokolada, " čokolade ,a ostane ti", round(ostatak_eura, 2), "eura.")
