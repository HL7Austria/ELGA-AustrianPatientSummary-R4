const tables_to_print = [
    { title: 'Allergien', table: i_allergies },
    { title: 'Aktuelle Medikamente', table: i_current_medication },
    { title: 'Vergangene Medikamente', table: i_past_medication },
    { title: 'Aktuelle Diagnose', table: i_current_problems },
    { title: 'Vergangene Diagnosen', table: i_past_problems },
    { title: 'Familienanamnese', table: i_family_problems },
    { title: 'Operationen', table: i_procedures },
    { title: 'Lebensstil', table: i_socialhistory },
    { title: 'Durchgeführte Tests', table: i_results },
    { title: 'Laborwerte', table: i_vitalsigns },
];


document.querySelector(".btn-print").addEventListener("click", function(){
    // need to load all tables into the DOM
    expandAll();
    printTables();
 });

 function printTables() {
    const print_area = document.createElement("div");

    // Static header and patient information
    const header_html = `
        <h1>IPS von Max Mustermann (m) - 11.12.1950</h1>
        <p>Adresse: Am Schulweg 5, Hainfeld, 3100, AUT</p>
        <p>Identifikationsnummer:0000121150</p>
    `;

    // Append the header to print_area
    print_area.innerHTML += header_html;

    // Loop through tables and add them to print_area
    for (const table_to_print of tables_to_print) {
        table_to_print.table.redraw(true); // Ensure table is redrawn
        const title_html = "<br>" + `<h2>${table_to_print.title}</h2>`;
        const table_html = table_to_print.table.getHtml();
        const sum_html = title_html + table_html ;

        print_area.innerHTML += sum_html;
    }

    // Create print window with header, patient info, and tables
    const printWindow = window.open('', '_blank');
    printWindow.document.open();
    printWindow.document.write(`
        <html>
        <head>
            <title>Print Multiple Tables</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }
                
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-bottom: 20px;
                }

                th, td {
                    border: 1px solid #333;
                    padding: 8px;
                    text-align: left;
                }

                th {
                    background-color: #f2f2f2;
                    font-weight: bold;
                }

                @page {
                    size: A4;
                    margin: 1cm;
                }

                h1 {
                    text-align: center;
                    font-size: 1.5em;
                    margin-bottom: 5px;
                }

                h2 {
                    text-align: center;
                    font-size: 1.2em;
                    margin-top: 20px;
                    margin-bottom: 10px;
                }

                p {
                    text-align: center;
                    margin: 0;
                    font-size: 1em;
                    margin-bottom: 5px;
                }

                @media print {
                    body {
                        -webkit-print-color-adjust: exact;
                        print-color-adjust: exact;
                    }
                }
            </style>
        </head>
        <body>${print_area.innerHTML}</body>
        </html>
    `);
    printWindow.document.close();
    printWindow.print();
}