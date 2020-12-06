import iomyfiles
from iomyfiles.helpers_plot import plot_kpi_comparison
from iomyfiles import WaveformsMatFilePC41, ExcelRequirements105

import tests.test_basic as tb

tb.test_plot_kpi_comparison()
tb.test_WaveformsMatFilePC41()
tb.test_ExcelRequirements105()
