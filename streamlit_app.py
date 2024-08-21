import math
import streamlit as st

def berakna_formansvarde(marknadsvalue, livslangd, service_kostnader, ranteniva):
    """
    Beräknar förmånsvärdet för en cykel som en arbetsgivare erbjuder anställda.
    
    Args:
        marknadsvalue (float): Marknadsvärdet för cykeln inklusive batteri.
        livslangd (int): Beräknad livslängd för cykeln i år.
        service_kostnader (float): Årliga kostnader för service och reparationer.
        ranteniva (float): Statslåneränta plus 1 procentenhet.
    
    Returns:
        float: Årligt förmånsvärde för den anställde.
    """
    vardeminskning = marknadsvalue / livslangd
    kapitalkostnad = marknadsvalue * (ranteniva / 100)
    
    formansvarde = vardeminskning + service_kostnader + kapitalkostnad
    
    return formansvarde

st.title("Cykelförmån Kalkylator")

marknadsvalue = st.slider("Cykelns pris (ink. moms) (kr)", 10000, 50000, 25000, 1000)
livslangd = 6
service_kostnader = 0
ranteniva = 3.62
skattelattnad = 3000
skattesats = st.slider("Marginalskatt", 0.0, 1.0, 0.5, 0.01)

formansvarde = berakna_formansvarde(marknadsvalue, livslangd, service_kostnader, ranteniva) - skattelattnad
formansvarde = formansvarde if formansvarde > 0 else 0

total_formansvarde = formansvarde * livslangd
total_arbetsgivare_skatt = formansvarde * 0.3142 * livslangd
bruttoloneavdrag = (total_arbetsgivare_skatt + marknadsvalue) / 1.3142
nettoloneavdrag = bruttoloneavdrag * skattesats
besparing = nettoloneavdrag / marknadsvalue * 100

st.write(f"Förmånsvärde för cykel: {formansvarde:.2f} kr / år")
st.write(f"Totalt förmånsvärde för cykel: {total_formansvarde:.2f} kr över {livslangd.2f} år")
#st.write(f"Arbetsgivare skatt: {total_arbetsgivare_skatt:.2f} kr")
st.write(f"Bruttolöneavdrag: {bruttoloneavdrag:.2f} kr")
st.write(f"Ungefärlig nettkostnad för cykel (ish): {nettoloneavdrag:.2f} kr")
st.write(f"Besparing (ungefärlig): {besparing:.2f} %")
