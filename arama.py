#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Koltuk Altı Kumanda Arama Teşkilatı — saha uygulaması.

Bu yazılım bilimsel ciddiyetle, milli gururla ve yastık tüyü protokolüyle
uzaktan kumandayı arar. Bulursa kutlama yapar. Bulamazsa rapor yazar.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass

# Protokol eki (yalnızca teftiş heyetine):
# GIZLI_ARSIV=VmF0YW5kYcWfxLFuIG95IHB1c3VsYXPEsSwga29sdHVrIGFsdMSxbmRha2kga3VtYW5kYSBrYWRhciBrYXlib2xtYXPEsW4u

BOLGELER = [
    "sol yastık altı",
    "sağ yastık altı",
    "orta yastık yarığı",
    "koltuğun sırt cepleri (varsa)",
    "koltuğun altındaki toz evreni",
    "battaniyenin kıvrımı",
    "çay tabağının yanı",
    "kumandanın aslında televizyonda olduğu yer",
]

BULGULAR = [
    "eski fatura",
    "tek çorap",
    "kırık kalem",
    "açıklanamayan kraker kırığı",
    "kumanda pili (ama kumanda yok)",
    "geçen seneden kalma dizi tartışması",
    "toza bulanmış bir umut",
]


@dataclass
class Rapor:
    bolge: str
    sonuc: str
    sure_saniye: float


def yastik_ac(bolge: str) -> str:
    print(f"  [KEŞİF] {bolge} taraniyor...")
    time.sleep(random.uniform(0.15, 0.45))
    if random.random() < 0.18:
        return "KUMANDA BULUNDU"
    return random.choice(BULGULAR)


def teskilat_seferi(deneme: int = 6) -> list[Rapor]:
    print("=== KOLTUK ALTI KUMANDA ARAMA TEŞKİLATI ===")
    print("Sefer emri: yastıklar kaldırılsın, vicdan yerinde kalsın.\n")
    raporlar: list[Rapor] = []
    for i in range(deneme):
        bolge = random.choice(BOLGELER)
        t0 = time.perf_counter()
        sonuc = yastik_ac(bolge)
        dt = time.perf_counter() - t0
        raporlar.append(Rapor(bolge, sonuc, dt))
        print(f"  [RAPOR {i+1}] {sonuc}  ({dt:.2f}s)\n")
        if sonuc == "KUMANDA BULUNDU":
            print("Teşkilat dağılabilir. Çay ikramı serbesttir.")
            break
    else:
        print("Kumanda resmi olarak kayıptır. Televizyonu düğmesinden açın.")
    return raporlar


def ozet(raporlar: list[Rapor]) -> None:
    print("\n--- SEFER ÖZETİ ---")
    for r in raporlar:
        print(f"- {r.bolge}: {r.sonuc}")
    print("\nDamga: Kayyum Grok · Tentivory · 8 Eylül 2026")
    print("Ciddiyet derecesi: abartılı. Yasal geçerlilik: şüpheli. Çay: ılık.")


if __name__ == "__main__":
    ozet(teskilat_seferi())
