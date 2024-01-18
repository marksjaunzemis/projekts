# projekts

Projekta mērķis ir izveidot programmu, ar kuras palīdzību es spētu automatizēt kādu darbību ko es izpildu savā ikdienā. Tā kā es strādāju darbu no mājām es izdomāju savu projektu saistīt ar savu darbu, lai atvieglotu sev darbu un ieekonomētu savu laiku. Viens no mana darba uzdevumiem sastāv no pdf failu saglabāšanas mapē un to failu pārsaukšanas uz cipariem sākot no 1 līdz tik cik faili ir šajā mapē.

Projekta uzdevums ir pārsaukt visus pdf failus kuri atrodas noteiktā mapē, lai pirmais ievietotais pdf fails arī tiku nosaukts "1" u.t.t. Šis projekts man atvieglos darbu un ietaupīs laiku, jo man nebūs katru failu jāpārsauc atsevišķi, un man nevarēs rasties nekādas cilvēciskas kļūdas kur es pārsaucu kādu failu par nepareizo ciparu. Tā kā noteiktajā mapē pdf faili jau būs pareizajā secībā, man tos nav nepieciešams organizēt savādāk.

Rakstot šo programmu es izmantoju tikai "os" moduli, kas man ļauj mijiedarboties ar operētājsistēmu, jo viss nepieciešamais man jau atrodas uz datora, un tā kā man nav nepieciešams veikt citas darbības kā failu filtrēšanu vai kārtošanu, man nav nepieciešamas citas bibliotēkas. Šis arī padara programmu "vieglāku" datoram un neprasa daudz datora līdzekļu.

Programma ir jāsaglabā datorā, piemēram, "rename_pdfs.py", pēc tam ir jāsagatavo mape ar visiem pdf failiem. Lai palaistu scriptu vajag izmantot datora termināli un palaist skriptu izmantojot "python rename_pdfs.py", un tad ir jāieraksta ceļš uz noteikto mapi ar pdf failiem. Pec tam skripts pārsauks pdf failus sākot ar 1, tas arī izvadīs veco pdf faila nosaukumu un jauno, kā arī beigās tiks izvadīts kopējais pārsaukto pdf failu skaits
