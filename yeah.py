import platform
from platform import architecture, machine, mac_ver, system
from os import environ

# Example function to normalize architecture
def normalize_architecture(architecture):
    if architecture == "x86_64" or architecture == "64bit":
        return "64-bit"
    elif architecture == "arm64":
        return "Arm64"
    return architecture

# Function to retrieve system information
def get_system_info():
    sys = system()

    if sys == "Windows":
        from platform import win32_ver, win32_edition
        win_version, win_release, _, _ = win32_ver()
        win_edition = win32_edition()
        arch = architecture()[0]
        arch = normalize_architecture(arch)
        return f"Windows {win_version} {win_edition} {arch}"

    elif sys == "Linux":
        try:
            from platform import freedesktop_os_release
            distro_info = freedesktop_os_release()
            pretty_name = distro_info.get("PRETTY_NAME", "")
            version = distro_info.get("VERSION", "")
            version_id = distro_info.get("VERSION_ID", "")
            arch = architecture()[0]
            arch = normalize_architecture(arch)

            if pretty_name:
                return f"{pretty_name} {arch}"
            elif version:
                return f"{version} {arch}"
            else:
                name = distro_info.get("NAME", "Linux")
                if version_id:
                    return f"{name} {version_id} {arch}"
                else:
                    return f"{name} {arch}"

        except OSError:
            return f"Linux {architecture()[0]}"

    elif sys == "Darwin":
        mac_version = mac_ver()[0]
        arch = machine()
        arch = normalize_architecture(arch)
        return f"macOS {mac_version} {arch}"

    else:
        return "Unable to get OS information (っ °Д °;)っ"

if __name__ == "__main__":
    print("System Information:")
    print(get_system_info())
