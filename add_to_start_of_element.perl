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
use HTML::TreeBuilder;
use HTML::Element;

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

# Taks 2 args

sub main {
    my ($arg, $h1_string) = @_;
    
    my $content = read_text($arg);
    my $root = HTML::TreeBuilder->new_from_content($content);

    my $target_class = "entry-content";

    my $h1 = HTML::Element->new('h1');
    $h1->push_content($h1_string);

    my $match = $root->look_down(class => $target_class);

    $match->unshift_content($h1);

    open my $fh, ">", $arg or die $!;
    say $fh $root->as_HTML;
    close $fh or die $!;
}

main @ARGV;
