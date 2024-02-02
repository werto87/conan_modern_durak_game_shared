from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import get

required_conan_version = ">=1.51.1"


class ConanHeaderOnly(ConanFile):
    name = "modern_durak_game_shared"
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps", "CMakeToolchain"

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def configure(self):
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, "20")
        self.options["boost"].header_only = True
        self.options["fmt"].header_only = True

    def requirements(self):
        self.requires("durak/1.0.0")
        self.requires("confu_json/1.0.1")

    def layout(self):
        cmake_layout(self, src_folder=self.name + "-" + str(self.version))

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()
