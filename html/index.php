<html>
    <head>
        <title>USH Informatica - Front</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="card text-center">
            <h5 class="card-header">
                Lista completa
            </h5>
            <div class="card-body">
                <p class="card-text">In cazul in care doresti sa iti actualizezi pozitia in lista,
                introdu numele si selecteaza o alta ora pentru acelasi laborator.
                In cazul in care doresti sa te stergi de la un laborator, introdu numele
                si selecteaza optiunea de "Stergere din lista".</p>
                <a href="/results" class="btn btn-primary">Apasa aici pentru a vizualiza lista</a>
            </div>
        </div>
        <div class="card text-center">
            <h5 class="card-header">
                Completeaza in functie de locul dorit
            </h5>
            <div class="card-body">
                <p class="card-text">Ai grija sa iti introduci numele corect!</p>
                <form action="/submit" method="post" accept-charset="utf-8">
                    <label for="name"><b>Nume intreg:</b></label><br>
                    <input type="text" id="name" name="name" autocomplete="off" placeholder="Ex: Popescu Ion" required pattern="\b(?!.*?\s{2})[A-Za-z ]+\b"><br>
                    <label for="select"><b>Ziua si ora:</b></label><br>
                    <select id="select" name="select">
                        <optgroup label="Fundamentele Programarii">
                            <option value="FP_LUNI 08-10">LUNI 8-10</option>
                            <option value="FP_LUNI 10-12">LUNI 10-12</option>
                            <option value="FP_LUNI 12-14">LUNI 12-14</option>
                            <option value="FP_LUNI 14-16">LUNI 14-16</option>
                            <option value="FP_LUNI 16-18">LUNI 16-18</option>
                            <option value="FP_VINERI 10-12">VINERI 10-12</option>
                            <option value="FP_VINERI 12-14">VINERI 12-14</option>
                            <option value="FP_VINERI 14-16">VINERI 14-16</option>
                            <option value="FP_DELETE">Stergere din lista</option>
                        </optgroup>
                        <optgroup label="Arhitectura Sistemelor de Calcul">
                            <option value="ASC_VINERI 10-12">VINERI 10-12</option>
                            <option value="ASC_VINERI 12-14">VINERI 12-14</option>
                            <option value="ASC_VINERI 14-16">VINERI 14-16</option>
                            <option value="ASC_VINERI 16-18">VINERI 16-18</option>
                            <option value="ASC_VINERI 18-20">VINERI 18-20</option>
                            <option value="ASC_SAMBATA 14-16">SAMBATA 14-16</option>
                            <option value="ASC_SAMBATA 16-18">SAMBATA 16-18</option>
                            <option value="ASC_SAMBATA 18-20">SAMBATA 18-20</option>
                            <option value="ASC_DELETE">Stergere din lista</option>
                        </optgroup>
                    </select>
                    <input class="btn btn-primary" type="submit" value="Trimite">
                </form>
            </div>
            <?php
            $success = $_GET['success'];
            if (isset($success))
            {
                if ($success == 'true')
                {
                    ?>
                    <center>
                        <div class="alert alert-success alert-dismissible w-50">
                            <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
                            <strong>SUCCESS!</strong> Datele tale au fost actualizate.
                        </div>
                    </center>
                    <?php
                }
                elseif ($success == 'false')
                {
                    ?>
                    <center>
                        <div class="alert alert-danger alert-dismissible w-50">
                            <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
                            <strong>ERROR!</strong> Ceva nu a mers cum trebuie. Te rog incearca din nou.
                        </div>
                    </center>
                    <?php
                }
            }
            ?>
        </div>
        <div class="footer-copyright text-center">Fully coded in Python - &copy; Copyright 2020
            <a href="https://eduardgro.su"> eduardgro.su</a>
        </div>
    </body>
</html>
