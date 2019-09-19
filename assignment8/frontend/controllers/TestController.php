<?php

namespace frontend\controllers;

use yii\web\Controller;

class TestController extends Controller
{
    public function actionIndex() 
    {
        $data = 'test';
        return $this->render('index');

    }

    public function actionTest()
    {
        echo 'Sukan';
        return $this->render('test');
    }
}
