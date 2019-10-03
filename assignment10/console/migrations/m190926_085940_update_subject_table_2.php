<?php

use yii\db\Migration;

/**
 * Class m190926_085940_update_subject_table_2
 */
class m190926_085940_update_subject_table_2 extends Migration
{
    /**
     * {@inheritdoc}
     */
    public function safeUp()
    {
        $this->dropColumn('subject', 'create_at');
        $this->dropColumn('subject', 'create_by');
        $this->dropColumn('subject', 'updated_at');
        $this->dropColumn('subject', 'updated_by');

        $this->addColumn('subject', 'created_at', $this->integer());
        $this->addColumn('subject', 'created_by', $this->integer());
        $this->addColumn('subject', 'updated_at', $this->integer());
        $this->addColumn('subject', 'updated_by', $this->integer());

    }

    /**
     * {@inheritdoc}
     */
    public function safeDown()
    {
        echo "m190926_085940_update_subject_table_2 cannot be reverted.\n";

        return false;
    }

    /*
    // Use up()/down() to run migration code without a transaction.
    public function up()
    {

    }

    public function down()
    {
        echo "m190926_085940_update_subject_table_2 cannot be reverted.\n";

        return false;
    }
    */
}
