import subprocess

process = subprocess.Popen("adb shell", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

commands = [
    "uname -a",
    "getprop ro.build.version.security_patch",
    "getprop ro.build.version.release",

]

for command in commands:
    process.stdin.write(command + "\n")
process.stdin.close()
output, error = process.communicate()
print("Output: Kernel,SPL,Android_version \n", output)
print("Error:", error)