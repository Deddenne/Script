@echo off

>output.txt (
    echo AIO-401-001 - 10.2.101.3
    md "\\10.2.101.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.101.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-401-001 - 10.3.6.12
    md "\\10.3.6.12\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.3.6.12\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-401-002 - 10.2.101.12
    md "\\10.2.101.12\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.101.12\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-401-8 - 10.3.6.23
    md "\\10.3.6.23\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.3.6.23\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LP-401-7 - 10.2.101.7
    md "\\10.2.101.7\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.101.7\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TPV-401-001 - 10.2.101.1
    md "\\10.2.101.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.101.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-421-12 - 10.2.121.3 ou 10.2.121.5
    md "\\10.2.121.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.121.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-421-14 - 10.2.121.1
    md "\\10.2.121.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.121.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-421-17 - 10.2.121.13
    md "\\10.2.121.13\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.121.13\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-421-19 - 10.2.121.16
    md "\\10.2.121.16\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.121.16\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-421-20 - 10.2.121.33 ou 10.2.121.33
    md "\\10.2.121.33\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.121.33\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LP-421-13 - 10.2.121.4
    md "\\10.2.121.4\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.121.4\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LP-421-15 - 10.2.121.2
    md "\\10.2.121.2\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.121.2\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LP-421-16 - 10.2.121.3
    md "\\10.2.121.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.121.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TPV-403-001 - 10.2.103.1
    md "\\10.2.103.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.103.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TPV-404-001 - 10.2.104.3
    md "\\10.2.104.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.104.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LP-406-7 - 10.2.106.10 ou 10.2.106.11
    md "\\10.2.106.10 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.106.10 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-408-001 - 10.2.108.4 
    md "\\10.2.108.4 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.108.4 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TPV-408-001 - 10.2.108.1
    md "\\10.2.108.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.108.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TPV-408-002 - 10.2.108.2
    md "\\10.2.108.2\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.108.2\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-418-4 - 10.2.118.3
    md "\\10.2.118.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.118.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LP-418-4 - 10.2.118.5 ou 10.2.118.6 
    md "\\10.2.118.5\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.118.5\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-422-001 - 10.2.122.3 ou 10.2.122.6
    md "\\10.2.122.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.122.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-422-002 - 10.2.122.7 
    md "\\10.2.122.7 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.122.7 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-422-003 - 10.2.122.5 
    md "\\10.2.122.5 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.122.5 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TPV-422-001 - 10.2.128.7 
    md "\\10.2.128.7\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.128.7\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TPV-422-002 - 10.2.122.2
    md "\\10.2.122.2\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.122.2\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-426-3 - 10.2.126.7 ou 10.2.126.8
    md "\\10.2.126.7 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.126.7 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LP-426-2 - 10.2.106.2
    md "\\10.2.106.2\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.106.2\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-428-001 - 10.2.128.5
    md "\\10.2.128.5\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.128.5\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LP-428-1 - 10.2.128.1 ou 10.2.128.2
    md "\\10.2.128.1 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.128.1 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LP-428-4 - 10.2.128.7
    md "\\10.2.128.7\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.128.7\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TAB-428-001 - 10.2.128.95
    md "\\10.2.128.95\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.128.95\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TPV-428-002 - 10.2.128.1
    md "\\10.2.128.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.128.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LP-429-1 - 10.2.129.1 ou 10.2.129.2
    md "\\10.2.129.1 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.129.1 \c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LAP-438-001 - 10.2.138.3
    md "\\10.2.138.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.138.3\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TAB-438-001 - 10.2.138.95
    md "\\10.2.138.95\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.138.95\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TPV-438-001 - 10.2.138.1
    md "\\10.2.138.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.138.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TPV-438-002 - 10.2.138.2
    md "\\10.2.138.2\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.138.2\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo LP-454-2 - 10.3.103.30
    md "\\10.3.103.30\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.3.103.30\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"

    echo TPV-454-001 - 10.2.154.1
    md "\\10.2.154.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    xcopy "\\srv-data\Informatique\13-Distrib\Nepting" "\\10.2.154.1\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"


)