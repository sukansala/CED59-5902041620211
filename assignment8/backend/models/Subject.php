<?php
namespace backend\models;

use yii\behaviors\TimestampBehavior;
use yii\behaviors\BlameableBehavior;

class Subject extends \common\models\Subject
{
    public function behaviors()
    {
        return 
        [
            TimestampBehavior::class,
            BlameableBehavior::class
        ];
    }

    public function rules() 
    {
        return[
            ['name', 'required', 'message' => 'Please fill data.'],
            ['name', 'email', 'message' => 'Please type email.']
        ];
    }
}