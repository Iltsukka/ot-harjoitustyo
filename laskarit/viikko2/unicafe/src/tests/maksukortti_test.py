import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        kortti = self.maksukortti
        self.assertNotEqual(str(kortti), None)
    
    def test_saldo_alussa_oikein(self):
        kortti = self.maksukortti
        self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        kortti = self.maksukortti
        kortti.lataa_rahaa(200)
        self.assertEqual(str(kortti), "Kortilla on rahaa 12.00 euroa")

    def test_saldo_vähenee_jos_rahaa(self):
        kortti = self.maksukortti
        kortti.ota_rahaa(500)
        self.assertEqual(str(kortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_vähene_jos_ei_rahaa(self):
        kortti = self.maksukortti
        kortti.ota_rahaa(1500)
        self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_false(self):
        x = self.maksukortti.ota_rahaa(1500)
        self.assertFalse(x)
    
    def test_metodi_palauttaa_true(self):
        x=self.maksukortti.ota_rahaa(900)
        self.assertTrue(x)
    
    