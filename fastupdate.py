#!/usr/bin/python

import sys, os

FASTBOOT = "fastboot "
WORKBASE = "/reposi/project/softap/M9615R2020/"

images = {'boot': WORKBASE + "apps_proc/oe-core/build/tmp-eglibc/deploy/images/9615-cdp/boot-oe-msm9615.img",
          'aboot': WORKBASE + "apps_proc/oe-core/build/tmp-eglibc/deploy/images/9615-cdp/appsboot.mbn",
          'userdata': WORKBASE + "apps_proc/oe-core/build/tmp-eglibc/deploy/images/9615-cdp/9615-cdp-usr-image.usrfs.yaffs2",
          'system': WORKBASE + "apps_proc/oe-core/build/tmp-eglibc/deploy/images/9615-cdp/9615-cdp-image-9615-cdp.yaffs2",
          'recovery': WORKBASE + "apps_proc/oe-core/build/tmp-eglibc/deploy/images/9615-cdp/recovery-boot-oe-msm9615.img",
          'recoveryfs': WORKBASE + "apps_proc/oe-core/build/tmp-eglibc/deploy/images/9615-cdp/9615-cdp-recovery-image-9615-cdp.yaffs2",
          'dsp1': WORKBASE + "modem_proc/build/ms/bin/ACETWMAZ/dsp1.mbn",
          'dsp2': WORKBASE + "modem_proc/build/ms/bin/ACETWMAZ/dsp2.mbn",
          'dsp3': WORKBASE + "lpass_proc/obj/qdsp6v4_ReleaseG/dsp3.mbn"
          }

if len(sys.argv) <= 1:
    print "You must give a parameter like boot, aboot, userdata, system"
    print "Usage: "
    print sys.argv[0] + " boot aboot userdata"
    print sys.argv[0] + " all"
    exit(1)

print "Your working base dir is " + WORKBASE

keys = sys.argv[1:]

if keys[0] == "all":
    for item in images.items():

        if os.access(item[1], False) == False:
            print item[1] + " File does not exist. Abort update"
            exit(1)
        erase_cmd = FASTBOOT + "erase " + item[0]
        flash_cmd = FASTBOOT + "flash " + item[0] + " " + item[1]

        print "Erasing " + item[0] + " partition."
        os.system(erase_cmd)

        print "Fusing " + item[0] + " partition."
        os.system(flash_cmd)

        print item[0] + " partitions update done. Good luck"
    os.system(FASTBOOT + " reboot")
    exit(0)


for key in keys:
    if key in images:
        file = images[key]
    else:
        print key + " is wrong key string."
        print "Available key string is:"
        print ""
        print "boot aboot userdata system"
        exit(1)

        if os.access(file, False) == False:
            print "Updated file does not exist."
            exit(1)

    erase_cmd = FASTBOOT + "erase " + key
    flash_cmd = FASTBOOT + "flash " + key + " " + file

    print "Erasing " + key + " partition."
    os.system(erase_cmd)

    print "Fusing " + key + " partition."
    os.system(flash_cmd)

    print key + " partition update done. Good luck"

os.system(FASTBOOT + " reboot")
exit(0)
