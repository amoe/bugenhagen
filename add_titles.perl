#! /usr/bin/perl
use strict;
use warnings;
use v5.20.2;
use Data::Dump qw/dump/;
use File::Slurper qw/read_text/;
use Getopt::Long;
use autodie qw(:all);
use Log::Any qw($log);
use Log::Dispatch;
use Log::Any::Adapter;
use utf8;

binmode(STDOUT, ':utf8');


sub init_logging {
    # Send all logs to Log::Dispatch
    my $dispatch_logger = Log::Dispatch->new(
        outputs => [
            [ 'Screen', min_level => 'debug', newline => 1 ],
        ],
    );
    Log::Any::Adapter->set('Dispatch', dispatcher => $dispatch_logger);
}

init_logging();
$log->debugf("arguments are: %s", "foo");


my $data   = "file.dat";
my $length = 24;
my $verbose;

GetOptions ("length=i" => \$length,    # numeric
            "file=s"   => \$data,      # string
            "verbose"  => \$verbose)   # flag
    or die("Error in command line arguments\n");

sub main {
    my ($db_file) = @_;

    open my $fh, '<', $db_file or die $!;

    while (<$fh>) {
        chomp;

        my ($file, $title) = /([^\t]*)\t(.*)/;

        $file =~ s|/index\.html$|.xhtml|;
        $file =~ s|^./||;

        say "$file";
        say "$title";

        system(
            "/usr/bin/perl",
            "/home/amoe/dev/scriptpool/add_to_start_of_element.perl",
            "/home/amoe/ebooks/diggler/content/" . $file,
            $title
        );
    }

    close $fh or die $!;
}

main @ARGV;
