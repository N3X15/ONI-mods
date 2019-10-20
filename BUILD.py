from buildtools.maestro import BuildMaestro
from buildtools.maestro.base_target import SingleBuildTarget
from buildtools.config import TOMLConfig
from buildtools.maestro.convert_data import ConvertDataBuildTarget, EDataType
from buildtools.maestro.fileio import ReplaceTextTarget, CopyFileTarget, CopyFilesTarget
from buildtools.maestro.shell import CommandBuildTarget
from buildtools.buildsystem.msbuild import MSBuild
from buildtools import os_utils, log
import os, sys
from typing import Dict, List
devenv = r'C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe'
CONFIG = TOMLConfig('build-config.toml', default={
    'paths': {
        'vs-dir':    os.path.join('C:\\', 'Program Files (x86)', 'Microsoft Visual Studio', '2019', 'Community'),
        'oni':       os.path.join('C:\\', 'Program Files (x86)', 'Steam', 'SteamApps', 'common', 'OxygenNotIncluded'),
        'oni-mods':  os.path.join(os.path.expanduser('~'), 'Documents', 'Klei', 'OxygenNotIncluded', 'mods')
    },
})

ENV = os_utils.ENV.clone()

LOCALMODS = os.path.join(CONFIG.get('paths.oni-mods'), 'dev')
# C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Current\Bin\amd64\MSBuild.exe
MSBUILD = os.path.join(CONFIG.get('paths.vs-dir'), 'MSBuild', 'Current', 'Bin', 'amd64', 'MSBuild.exe')

class MSBuildTarget(SingleBuildTarget):
    BT_LABEL = 'MSBUILD'
    def __init__(self, target: str, solution: str, files: List[str], configuration: str = None, properties: Dict[str, str] = {}, dependencies=[], msbuild_executable=MSBUILD):
        self.msbuild_executable=msbuild_executable
        self.msb = MSBuild()
        self.msb.solution = solution
        self.msb.configuration = configuration
        self.msb.properties = properties
        super().__init__(target, files=[solution]+files, dependencies=dependencies)

    def build(self):
        self.msb.run(MSBUILD=self.msbuild_executable)

def mkproject(bm: BuildMaestro, project: str, depends: List[str] = []):
    with log.info('Configuring %s...', project):
        dll = os.path.join('src', project, 'bin', project+'.dll')
        proj_dir = os.path.join('src', project)
        csfiles = [f for f in os_utils.get_file_list(os.path.join(proj_dir, 'Source')) if f.endswith('.cs')]
        csp = bm.add(MSBuildTarget(dll, os.path.join(proj_dir, f'{project}.sln'), csfiles, dependencies=depends))
        csp.msb.properties['ONIPath'] = CONFIG.get('paths.oni')

        deploydir = os.path.join(LOCALMODS, project)
        bm.add(CopyFileTarget(deploydir, dll, dependencies=[csp.target]))
        os_utils.ensureDirExists(deploydir, noisy=True)
        for basefilename in os.listdir(os.path.join('Mods', project)):
            filename = os.path.join('Mods', project, basefilename)
            _, ext = os.path.splitext(basefilename)
            if ext in ('.json', '.txt'):
                cf = bm.add(CopyFileTarget(os.path.join(deploydir, basefilename), filename, dependencies=[csp.target], verbose=True))
                log.info('Found config: %s', basefilename)
        return csp


bm = BuildMaestro()
mkproject(bm, 'BlackHoleGarbageDisposal')
mkproject(bm, 'CoalGenerator')
mkproject(bm, 'HalfDoor')
mkproject(bm, 'HighFlowStorage')
mkproject(bm, 'MoreTemperatureSensors')
mkproject(bm, 'PipedOutput')
mkproject(bm, 'PipePressureValve')
mkproject(bm, 'PlayerControlledSwitch')
mkproject(bm, 'WaterSieveDynamicClone')
bm.as_app()
