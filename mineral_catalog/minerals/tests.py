from django.test import TestCase
from django.core.urlresolvers import reverse
import unittest

from .models import Mineral


mineral_one = {
    "name": "Adamite",
    "image_filename": "240px-Adamite-179841.jpg",
    "image_caption": "Yellow-green adamite in limonite",
    "category": "Arsenate",
    "formula": "Zn<sub>2</sub>AsO<sub>4</sub>OH",
    "strunz_classification": "08.BB.30",
    "crystal_system": "Orthorhombic Dipyramidal H-M Symbol (2/m 2/m 2/m) Space Group: Pnnm",
    "color": "Pale yellow, honey-yellow, brownish yellow, reddish; rarely white, colorless, blue, pale green to green, may be zoned;",
    "cleavage": "{101}, good; {010}, poor",
    "mohs_scale_hardness": "3.5",
    "luster": "Vitreous",
    "streak": "white to pale green",
    "optical_properties": "Biaxial (+/-)",
    "refractive_index": "nα=1.708 - 1.722, nβ=1.742 - 1.744, nγ=1.763 - 1.773",
    "crystal_habit": "Wedge-like prisms typically in druses and radiating clusters - also smooth botryoidal masses.",
    "specific_gravity": "4.32–4.48 measured",
    "group": "Arsenates"
}

mineral_two = {
    "name": "Aegirine",
    "image_filename": "250px-8336M-aegirine.jpg",
    "image_caption": "Monoclinic crystal of aegirine with orthoclase, from Mount Malosa, Zomba District, Malawi (size: 85 mm x 83 mm; 235 g)",
    "category": "Silicate, Pyroxene",
    "formula": "<sub>231</sub>.<sub>00</sub>",
    "strunz_classification": "09.DA.25",
    "crystal_system": "Monoclinic Prismatic",
    "unit_cell": "a = 9.658 Å, b = 8.795 Å, c = 5.294 Å, β = 107.42°; Z=4",
    "color": "Dark Green, Greenish Black",
    "crystal_symmetry": "Monoclinic 2/m",
    "cleavage": "Good on {110}, (110) ^ (110) ≈87°; parting on {100}",
    "mohs_scale_hardness": "6",
    "luster": "Vitreous to slightly resinous",
    "streak": "Yellowish-grey",
    "diaphaneity": "Translucent to opaque",
    "optical_properties": "Biaxial (-)",
    "refractive_index": "nα = 1.720 - 1.778 nβ = 1.740 - 1.819 nγ = 1.757 - 1.839",
    "crystal_habit": "Prismatic crystals may be in sprays of acicular crystals, fibrous, in radial concretions",
    "specific_gravity": "3.50 - 3.60",
    "group": "Silicates"
}


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral_one = Mineral.objects.create(**mineral_one)
        self.mineral_two = Mineral.objects.create(**mineral_two)

    # def test_mineral_list_view(self):
    #     resp = self.client.get(reverse('minerals:list'))
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(self.mineral_one, resp.context['minerals'])
    #     self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
    #     self.assertContains(resp, self.mineral_one.name)

    # def test_mineral_detail_view(self):
    #     resp = self.client.get(reverse(
    #         'minerals:detail',
    #         kwargs={'pk': self.mineral_two.pk}
    #     ))
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(self.mineral_two.name, resp.context['mineral'].values())

    # def test_mineral_list_sort_by_group(self):
    #     resp = self.client.get(reverse(
    #         'minerals:group',
    #         kwargs={'group': 'Arsenates'}
    #     ))
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(self.mineral_one, resp.context['minerals'])
    #     self.assertNotIn(self.mineral_two, resp.context['minerals'])

    # def test_search_by_term(self):
    #     resp = self.client.get(reverse('minerals:search'), {'q': 'adamite'})
    #     resp2 = self.client.get(reverse('minerals:search'), {'q': 'aegirine'})
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(self.mineral_one, resp.context['minerals'])
    #     self.assertTemplateUsed(resp, 'minerals/mineral_list.html')

    def test_search_by_letter(self):
        resp = self.client.get(reverse('minerals:letter'), kwargs={'letter': 'a'})
        self.assertEqual(resp.status_code, 200)






























































