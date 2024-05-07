# Импортируем расширения, если они используются
import sphinx_rtd_theme

# Настройки для сборки документации

# Путь к документации в исходном коде
source_suffix = '.rst'
master_doc = 'index'

# Настройки темы
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
