#!/usr/bin/env python
# -*- encoding=utf-8 -*-

"""Unittest for aircv."""


import unittest
from airtest.aircv import imread
from airtest.aircv.keypoint_matching import *  # noqa
from airtest.aircv.keypoint_matching_contrib import *  # noqa
from airtest.aircv.template_matching import *  # noqa
from airtest.aircv.sift import find_sift
from airtest.aircv.template import find_template, find_all_template


class TestAircv(unittest.TestCase):
    """Test aircv."""

    THRESHOLD = 0.7
    RGB = True

    @classmethod
    def setUpClass(cls):
        cls.keypoint_sch = imread("matching_images/keypoint_search.png")
        cls.keypoint_src = imread("matching_images/keypoint_screen.png")

        cls.template_sch = imread("matching_images/template_search.png")
        cls.template_src = imread("matching_images/template_screen.png")

    @classmethod
    def tearDownClass(cls):
        pass

    def test_find_template(self):
        """Template matching."""
        result = TemplateMatching(self.template_src, self.template_sch, threshold=self.THRESHOLD, rgb=self.RGB).find_best_result()
        self.assertIsInstance(result, dict)

    def test_find_all_template(self):
        """Template matching."""
        result = TemplateMatching(self.template_src, self.template_sch, threshold=self.THRESHOLD, rgb=self.RGB).find_all_results()
        self.assertIsInstance(result, list)

    def test_find_kaze(self):
        """KAZE matching."""
        result = KAZEMatching(self.keypoint_src, self.keypoint_sch, threshold=self.THRESHOLD, rgb=self.RGB).find_best_result()  # 较慢,稍微稳定一点
        self.assertIsInstance(result, dict)

    def test_find_brisk(self):
        """BRISK matching."""
        result = BRISKMatching(self.keypoint_src, self.keypoint_sch, threshold=self.THRESHOLD, rgb=self.RGB).find_best_result()  # 快,效果一般,不太稳定
        self.assertIsInstance(result, dict)

    def test_find_akaze(self):
        """AKAZE matching."""
        result = AKAZEMatching(self.keypoint_src, self.keypoint_sch, threshold=self.THRESHOLD, rgb=self.RGB).find_best_result()  # 较快,效果较差,很不稳定
        self.assertIsInstance(result, dict)

    def test_find_orb(self):
        """ORB matching."""
        result = ORBMatching(self.keypoint_src, self.keypoint_sch, threshold=self.THRESHOLD, rgb=self.RGB).find_best_result()  # 很快,效果垃圾
        self.assertIsInstance(result, dict)

    def test_contrib_find_sift(self):
        """SIFT matching (----need OpenCV contrib module----)."""
        result = SIFTMatching(self.keypoint_src, self.keypoint_sch, threshold=self.THRESHOLD, rgb=self.RGB).find_best_result()  # 慢,最稳定
        self.assertIsInstance(result, dict)

    def test_contrib_find_surf(self):
        """SURF matching (----need OpenCV contrib module----)."""
        result = SURFMatching(self.keypoint_src, self.keypoint_sch, threshold=self.THRESHOLD, rgb=self.RGB).find_best_result()  # 快,效果不错
        self.assertIsInstance(result, dict)

    def test_contrib_find_brief(self):
        """BRIEF matching (----need OpenCV contrib module----)."""
        result = BRIEFMatching(self.keypoint_src, self.keypoint_sch, threshold=self.THRESHOLD, rgb=self.RGB).find_best_result()  # 识别特征点少,只适合强特征图像的匹配
        self.assertIsInstance(result, dict)

    def test_contrib_func_find_sift(self):
        """Test find_sift function in sift.py."""
        result = find_sift(self.keypoint_src, self.keypoint_sch, threshold=self.THRESHOLD, rgb=self.RGB)
        self.assertIsInstance(result, dict)

    def test_func_find_template(self):
        """Test find_template function in template.py."""
        result = find_template(self.template_src, self.template_sch, threshold=self.THRESHOLD, rgb=self.RGB)
        self.assertIsInstance(result, dict)

    def test_func_find_all_template(self):
        """Test find_all_template function in template.py."""
        result = find_all_template(self.template_src, self.template_sch, threshold=self.THRESHOLD, rgb=self.RGB)
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
