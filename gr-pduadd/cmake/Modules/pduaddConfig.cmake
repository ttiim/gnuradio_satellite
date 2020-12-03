INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PDUADD pduadd)

FIND_PATH(
    PDUADD_INCLUDE_DIRS
    NAMES pduadd/api.h
    HINTS $ENV{PDUADD_DIR}/include
        ${PC_PDUADD_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PDUADD_LIBRARIES
    NAMES gnuradio-pduadd
    HINTS $ENV{PDUADD_DIR}/lib
        ${PC_PDUADD_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/pduaddTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PDUADD DEFAULT_MSG PDUADD_LIBRARIES PDUADD_INCLUDE_DIRS)
MARK_AS_ADVANCED(PDUADD_LIBRARIES PDUADD_INCLUDE_DIRS)
