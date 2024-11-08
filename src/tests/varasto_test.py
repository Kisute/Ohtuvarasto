"""
Unit testit varasto luokalle.
"""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Testit luokalle"""

    def setUp(self):
        """Alustetaan 10:llä"""  
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
            """Testataan että konstruktori tekee tyhjän"""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Testataan että tehdyssä on oikea määrä tilaa"""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_tilavuus(self):
        """Testataan että negatiivista asetettaessa tilavuus menee nollaan"""
        varasto = Varasto(-5)
        self.assertAlmostEqual(varasto.tilavuus, 0)                       # "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa                   a"           

    def test_negatiivinen_alkusaldo(self):
        """Testataan että negatiivinen alku arvon saldo on 0"""
        varasto = Varasto(0, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        """Testataan että lisääminen lisää saldoa"""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Testataan että lisäys pienentää vapaata tilaa"""
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays(self):
        """Testataan että negatiivisen lisäys ei vaikuta"""
        self.varasto.lisaa_varastoon(-8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_liiallisen_lisays(self):
        """Testataan että liian lisääminen asettaa varan maksimiin"""
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Testataan että ottaminen palauttaa oikean verran"""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivisen_ottaminen_palauttaa_oikean_maaran(self):
        """Testataan että negatiivisen ottaminen palauttaa 0"""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_liian_ottaminen_palauttaa_oikean_maaran(self):
        """Testataan että liian ottaminen palauttaa vain saatavan"""
        self.varasto.lisaa_varastoon(6)
        saatu_maara = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(saatu_maara, 6)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ottaminen_lisaa_tilaa(self):
        """Testataan että ottaminen lisää tilaa"""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_esitys(self):
        """Testataan että esitys toimii"""
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")
