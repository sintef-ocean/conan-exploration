from os import path
from conan import ConanFile
from conan.tools.files import load, update_conandata
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.scm import Git

required_conan_version = ">=1.54"


class ExplorationConan(ConanFile):
    name = "exploration"
    description = "Test package for conanisation"
    settings = "os", "compiler", "build_type", "arch"
    package_type = "library"
    options = {
        "shared": [True, False],
        "fPIC": [True, False]
        }
    default_options = {
        "shared": False,
        "fPIC": True
    }
    exports = "version.txt"

    def set_version(self):
        version_file = path.join(self.recipe_folder, "version.txt")
        self.version = load(self, version_file).strip()

    def export(self):
        git = Git(self, self.recipe_folder)
        scm_url, scm_commit = git.get_url_and_commit()
        update_conandata(self, {"src": {"commit": scm_commit, "url": scm_url}})

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def source(self):
        git = Git(self)
        sources = self.conan_data["src"]
        git.clone(url=sources["url"], target=".")
        git.checkout(commit=sources["commit"])

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "both")
        self.cpp_info.set_property("cmake_file_name", "exploration")
        self.cpp_info.set_property("cmake_target_name", "exploration::exploration")
        self.cpp_info.libs = ["exploration"]
