import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
   
    def test_rahaa_kassassa_oikea_maara(self):
        
        kassa = Kassapaate()
        self.assertEqual(kassa.kassassa_rahaa, 100000)

    def test_edulliset_oikea_maara(self):
        kassa = Kassapaate()
        self.assertEqual(kassa.edulliset, 0)

    def test_maukkaat_oikea_maara(self):
        kassa = Kassapaate()
        self.assertEqual(kassa.maukkaat, 0)
    
    def test_syo_edullisesti_rahaa_riittavasti(self):
        kassa = Kassapaate()
        x = kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(x, 10)
    
    def test_syo_edullisesti_rahaa_ei_riittavasti(self):
        kassa = Kassapaate()
        x = kassa.syo_edullisesti_kateisella(230)
        self.assertEqual(x, 230)
    
    def test_syo_maukkaasti_kateisella(self):
        kassa = Kassapaate()
        x = kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(x, 100)
    
    def test_syo_maukkaasti_kateisella_raha_ei_riita(self):
        kassa = Kassapaate()
        x = kassa.syo_maukkaasti_kateisella(390)
        self.assertEqual(x, 390)

    def test_syo_edullisesti_kortilla(self):
        self.maksukortti = Maksukortti(1000)
        kassa= Kassapaate()
        x = kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(x)
    
    def test_syo_edullisesti_kortilla_ei_rahaa(self):
        self.maksukortti = Maksukortti(200)
        kassa= Kassapaate()
        x = kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertFalse(x)

    def test_maukkaasti_kortilla(self):
        self.maksukortti = Maksukortti(1000)
        kassa= Kassapaate()
        x = kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(x)
    
    def test_maukkaasti_kortilla_ei_rahaa(self):
        self.maksukortti = Maksukortti(200)
        kassa= Kassapaate()
        x = kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertFalse(x)

    def test_lataa_rahaa_kortille(self):
        self.maksukortti = Maksukortti(1000)
        kassa = Kassapaate()
        kassa.lataa_rahaa_kortille(self.maksukortti, 50)
        self.maksukortti.lataa_rahaa(50)
        self.assertEqual(kassa.kassassa_rahaa, 100050)
    
    def test_lataa_rahaa_kortille(self):
        self.maksukortti = Maksukortti(1000)
        kassa = Kassapaate()
        kassa.lataa_rahaa_kortille(self.maksukortti, 0)
        self.maksukortti.lataa_rahaa(0)
        self.assertEqual(kassa.kassassa_rahaa, 100000)
    
    def test_lataa_rahaa_kortille(self):
        self.maksukortti = Maksukortti(1000)
        kassa = Kassapaate()
        kassa.lataa_rahaa_kortille(self.maksukortti, -50)
        self.maksukortti.lataa_rahaa(-50)
        self.assertEqual(kassa.kassassa_rahaa, 100000)