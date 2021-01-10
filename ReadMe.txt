======================================================
TVK Data Tool v1.2
Copyright 2020, Han-Ting Lin. All rights reserved.
January 2021
======================================================

The TVK Data Tool software provides functions for cooperating the Temperature Verification Kit and Alpha model.. It takes the output .xls files from the software of t-View, and converts the data from temperature probes in to SeqGen temperature verification data table. 

This is for service engineers to operating temperature calibration for the thermal cycler purpose.

IMPORTANT: TVK Data Tool 1.0 is only for internal use, there will be more functions coming soon.

UPDATA: TVK Data Tool v1.2. Included dual channel function for both 384 and 96.

------------------------------------------------------
Requirements
------------------------------------------------------
** Windows operating system
** t-Viewer has been installed (To install t-Viewer, double click the t-View_Setup.exe and follow the instruction.)

******************************************************
Instruction for Recording Data
******************************************************

This temperature recording process dose not need to record or type it down one by one as before. Wasting too much time!!

Instead of big old gray probe module, we are using t-pod to communicate with computer program. 

By using the t-Viewer, the temperature data will be recorded automatically, if your setting is correct.

----------------------
Preset for t-Viewer
----------------------

1. Connect the thermal probe to the t-pod (RS-232), and connect the t-pod to engineer's computer.
2. Turn on the t-Viewer software and select the probe.
3. Go to "Tools > Settings > Data logging period" 
4. set the time step to 2 seconds, and press enter to set. (This is important, since the software has been set to read 2 sec time-step data.)
5. Tools > Settings > Graph > Select "Continuous Graph"

----------------------------
Let's Get Back to Machine
----------------------------

85 & 45 Degree Temperature Verification:

1. Push the button "Logging/ Chart" to start recording data (Software t-Viewer).
2. Turn on Temperature Verification on the thermal-cycler and start it.
3. When the 85 C Temperature Verification is done, pause the recording.
4. Export the data: Go to "File" extort the file .xls.
5. Close the "Temperature vs Time window" to terminate the recording.
6. For 45 C Temperature Verification and TNU test are the same procedure. (Repeat it from step 6)

**NOTE: You can run the program without TNU data for the calibration propose.

TNU Test:

1. Create the TNU test on the thermal cycler
2. Push the button "Logging/ Chart" to start recording data (Software t-Viewer).
3. Pause the recording after the 7th cycle (For the single block only. For the dual block, NO need to stop the program.)
4. Export the data: Go to "File" extort the file .xls.
5. Close the "Temperature vs Time window" to terminate the recording.

**NOTE: For dual block 9700 (including both 384-well and 96 well), measure as following sequence: 
        Right block 85C -> Left block 85C -> Left block 45C -> Right block 45C -> Right block TNU -> Left block TNU

------------------------------------------------------
Instruction for TVU Data Tool v1.2 Processing Data
------------------------------------------------------

1. Double click TVK Data tool.exe to start the software.
2. Select your block type. (For 7900 and 7500, select "Single")
2. Select the files for 85 C, 45 C, and TNU data (The .xls files) from your computer.
3. Click "Next" to process the data.
4. Then the software will generate the Temperature Verification Data Table and TNU Data Table.
5. This program also generate a temperature log file under the same directory with TVK Data Tool.exe, so you can check all cycles of TNU etc.
6. Done!

------------------------------------------------------
About Us
------------------------------------------------------

In 1998, founder and President of SeqGen, Inc., Dr. George Yang, began what was to become a continuing tradition of hard work and service excellence. His Ph.D. in Molecular Biology, coupled with an MBA and years of service experience, have provided customers with a resource they can rely on.

Since the early years, George has expanded his staff to include additional service engineers of equal experience and quality.

What began as a “one-man” operation has grown into an international network of service engineers. Our corporate headquarters are located in Los Angeles, CA.

More detail: https://seqgen.com/
